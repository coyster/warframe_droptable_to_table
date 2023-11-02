import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:/Program Files (x86)/chromedriver.exe"


class Promocode:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 5, poll_frequency=0.2)
        self.logged_in = False
        self.username, self.password = self.creds(
            "WARFRAME_USERNAME", "WARFRAME_PASSWORD"
        )

    def new_driver(self):
        self.driver = webdriver.Chrome()

    def creds(self, username_label, password_label):
        load_dotenv()
        return os.getenv(username_label), os.getenv(password_label)

    def open_browser(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        return driver

    def login(self):
        self.driver_check()
        print(self.driver)
        login_url = "https://www.warframe.com/login"
        self.driver.get(login_url)
        # driver = self.open_browser(login_url)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "fldEmail"))
        ).send_keys(self.username)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "fldPassword"))
        ).send_keys(self.password)

        self.driver.find_element(By.ID, "submit-login").click()

        self.wait.until(
            method=EC.staleness_of(self.driver.find_element(By.ID, "submit-login"))
        )
        self.logged_in = True

    def driver_check(self) -> None:
        if self.driver is None:
            self.new_driver()

    def login_check(self) -> None:
        if self.logged_in is False:
            _ = self.login()

    def success(
        self,
    ) -> bool:
        WebDriverWait(self.driver, 2)
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, "basicTextContain")))
            text = self.driver.find_element(By.ID, "basicTextContain").text
            if text == "Thanks for redeeming your code!":
                print(f"Success: {text}")
                return True
            else:
                return False

        except Exception as e:
            print(f"Error: {e}")
            return False

    def input_promocode(self, promocode) -> (str, bool):
        self.driver_check()
        self.login_check()

        promocode_url = "https://www.warframe.com/promocode"

        self.driver.get(promocode_url)

        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "promocode_input"))
        ).send_keys(promocode)

        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "btnSubmit"))
        ).click()

        self.wait.until(EC.staleness_of(self.driver.find_element(By.ID, "btnSubmit")))

        # self.driver.find_element(By.ID, "btnSubmit").click()
        return (promocode, self.success())


promocode_list = [
    "hacksmith-bot",
    "Pride2023",
    "PRIDE2023",
    "Zxpfer",
    "Zarionis",
    "YourLuckyClover",
    "xxVampixx",
    "Xenogelion",
    "Woxli",
    "WideScreenJohn",
    "WarframeWiki",
    "WarframeRunway",
    "WarframeCommunityDiscord",
    "Wanderbots",
    "VVhiteAngel",
    "VoltTheHero",
    "Voli",
    "VoidFissureBR",
    "Vernoc",
    "VashCowaii",
    "Varlinator",
    "Vamppire",
    "VAMP6X6X6X",
    "UnrealYuki",
    "Triburos",
    "TrashFrame",
    "ToxickToe",
    "TotalN3wb",
    "TioRamon",
    "TioMario",
    "TinBears",
    "TheKengineer",
    "TheGamio",
    "TennoForever",
    "TeaWrex",
    "TBGKaru",
    "TaticalPotato",
    "Tanchan",
    "Tanandra",
    "StudioCyen",
    "Strippin",
    "Sn0wRC",
    "Smoodie",
    "SkillUp",
    "SillFix",
    "Shul",
    "Sherpa",
    "ShenZhao",
    "Sharlazard",
    "SerdarSari",
    "ScarletMoon",
    "SarahTsang",
    "Sapmatic",
    "RustyFin",
    "RoyalPrat",
    "Ritens",
    "Rippz0r",
    "ReyGanso",
    "Relentlesszen",
    "RebelDustyPinky",
    "RainbowWaffles",
    "Rahetalius",
    "RagingTerror",
    "QTCC2",
    "QTCC",
    "Pyrah",
    "Purkinje",
    "ProfessorBroman",
    "PrimedAverage",
    "Pride2022",
    "PostiTV",
    "PocketNinja",
    "PlagueDirector",
    "Pandaah",
    "PammyJammy",
    "OrpheusDeluxe",
    "OriginalWickedFun",
    "OOSIJ",
    "OddieOwl",
    "NoSympathyy",
    "NineYear22",
    "MrSteelWar",
    "Mogamu",
    "MissFwuffy",
    "MikeTheBard",
    "MichelPostma",
    "MHBlacky",
    "McMonkeys",
    "McGamerCZ",
    "Makarimorph",
    "MadFury",
    "Macho",
    "LynxAria",
    "LiliLexi",
    "LeyzarGamingViews",
    "LeoDoodling",
    "LadyTheLaddy",
    "L1feWater",
    "Kretduy",
    "Kr1ptonPlayer",
    "Kiwad",
    "Kirarahime",
    "KingGothaLion",
    "KavatsSchroedinger",
    "K1llerBarbie",
    "JustRLC",
    "Joriale",
    "JoeyZero",
    "JessiThrower",
    "JamieVoiceOver",
    "IWoply",
    "InfoDiversao",
    "Ikedo",
    "IISlip",
    "Iflynn",
    "Hydroxate",
    "HotShomStories",
    "Homiinvocado",
    "HappinesDark",
    "H3DSH0T",
    "GrindHardSquad",
    "Golden",
    "GlamShatterSkull",
    "Gingy",
    "GermanCommunityDiscord",
    "Gara",
    "Frozenballz",
    "FrostyNovaPrime",
    "FromThe70s",
    "FloofyDwagon",
    "FeelLikeAPlayer",
    "FashionFrameIsEndGame",
    "FacelessBeanie",
    "ExtraCredits",
    "EmpryeanCap",
    "Emojv",
    "Elnoraeleo",
    "EliceGameplay",
    "ElGrineerExiliado",
    "ElDanker",
    "Eduiy16",
    "DNexus",
    "DkDiamantes",
    "DjTechLive",
    "Disfusional",
    "DimitriV2",
    "DillyFrame",
    "DeuceTheGamer",
    "Depths",
    "DeepBlueBeard",
    "Deejayknight",
    "DebbySheen",
    "DayJobo",
    "DatLoon",
    "DasterCreations",
    "DanielTheDemon",
    "Cpt_Kim",
    "CopyKavat",
    "Conquera2022",
    "CohhCarnage",
    "Cleonaturin",
    "Chelestra",
    "Char",
    "ChacyTay",
    "CGsKnackie",
    "CephalonSquared",
    "Casardis",
    "CaleyEmerald",
    "Bwana",
    "BurnBxx",
    "Brozime",
    "BrotherDaz",
    "Bricky",
    "BrazilCommunityDiscord",
    "BigJimID",
    "Aznitrous",
    "Avelna",
    "AshiSogiTenno",
    "AnnoyingKillah",
    "AnjetCat",
    "AngryUnicorn",
    "Amprov",
    "AlexanderDario",
    "AlainLove",
    "AGayGuyPlays",
    "AeonKnight86",
    "AdmiralBahroo",
]
promocode_results = {}
promocode = Promocode()
promocode.login()

while len(promocode_list) > 0:
    code = promocode_list.pop()
    print(f"Inputing {code} \n")
    result = promocode.input_promocode(code)
    promocode_results[result[0]] = result[1]
    print(promocode_results)


# promocode.input_promocode()
