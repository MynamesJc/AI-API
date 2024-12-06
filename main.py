import speech_recognition as sr
import flet
from flet import *
import time
import openai
import pyttsx3
import requests

openai.api_key='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'
engine = pyttsx3.init()
r = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

class botHouse:
    def __init__(self):
        self.botHouse = Container(
            width=630,
            bgcolor="transparent",
            height=210,
            padding=padding.only(right=15),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.END,
                controls=[
                    Image(
                        src=f"bot.png",
                        width=70,
                        height=210,
                        border_radius=50,
                        repeat=ImageRepeat.NO_REPEAT,
                    )
                ],
            ),
        )

class mainInterface:
    def __init__(self, page):
        self.page = page

        #Search zone
        self.searchSource = "Google"
        self.sourceHIcon = icons.G_MOBILEDATA_ROUNDED
        self.searchHead = Container(
            height=70,
            border=border.all(width=2,color="white"),
            border_radius=15,
            padding=padding.only(left=10),
            bgcolor="white",
            content=Column(
                controls=[
                   Row(
                alignment="spaceBetween",
                controls=[
                    Text(
                        self.searchSource,
                        weight="bold",
                        color="blue",
                        size=20,
                    ),
                    Icon(
                        self.sourceHIcon,
                        size=50
                        )
                        ]
                    ),
                   Container(
                       margin=margin.only(top=-25),
                       content=Row(
                           alignment = "center",
                           controls=[
                               Text(
                                "La plus belle au monde ?",
                                color="black"
                                )
                           ]
                       )
                   )
                ]
            )
        )
        self.actionsbtn_card = Row(
            scroll="auto",

        )
        Btn = ['Tous','Images','Videos','actualites']

        for index in range(4):
             self.actionsbtn_card.controls.append(
                 Container(
                     padding=5,
                     border=border.all(width=1,color="white"),
                     border_radius=10,
                     margin=margin.only(left=5,right=5),
                     content=Text(
                        Btn[index],
                        size=15
                     )
                 )
            )
        self.gt = []
        self.gl = []
        self.gd = []
        self.gi = []



        self.resultAll=Column()
        self.contentsAll = Column(
            scroll="auto",
            height=390,
            controls=[
             self.resultAll
            ]
        )



        for index in range(len(self.gt)):
            self.urltext = Text(
                             self.gl[index],
                             color="grey",
                             size=12,
                             width=200,
                             height=20,
                          )

            self.resultAll.controls.append(
                Container(
                  bgcolor="white",
                  width=450,
                  border_radius=10,
                  padding=10,
                  margin=margin.only(bottom=5),
                  content=Column(
                      controls=[
                          Container(
                            on_click= lambda e:goTolinkPage(e),
                            content=self.urltext,
                          ),

                          Text(
                              self.gt[index],
                              color="blue",
                              size=16,
                          ),
                          Row(
                              alignment="spaceBetween",
                              controls=[
                            Column(
                                controls=[
                                Text(
                              self.gd[index],
                              width=160,
                              color="#616F79",
                              size=12,
                            ),
                                    ]),
                            Image(
                               src=self.gi[index],
                               width=100,
                               height=70,
                               fit=ImageFit.COVER,
                               repeat=ImageRepeat.NO_REPEAT,
                               border_radius=5,
                            )

                           ]
                         )
                      ]
                   )
                )
            )

        def goTolinkPage(e):
            self.page.launch_url(e.control.content.value)



        self.searchContent =  Container(
             height=435,
             width=450,
             content=Column(
             controls=[
               self.actionsbtn_card,
               self.contentsAll
             ]
            )
        )

        # Le chating zone
        self.objetSource =  "Conversation"
        self.sourceIcon = icons.CHAT_ROUNDED
        self.resultHead = Container(

            margin=margin.only(left=15, top=20),
            border_radius=15,
            height=50,
            padding=10,
            content=Row(
                alignment="spaceBetween",
                controls=[
                    Text(
                        #self.objetSource,
                        weight="bold",
                        size=15,
                    ),
                    Icon(
                        #self.sourceIcon,
                    )
                ]
            )
        )

        self.botText = Text(
                        "",
                        color="blue",
                        size=14,
                    )
        self.textControl = ListView(
                auto_scroll=True,
                controls=[
                    self.botText,
                ]
                )

        self.interactResponse = Container(
            visible=True,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=["white"],),
            border_radius=border_radius.only(
            top_left=20, top_right=20, bottom_left=20),
            margin=margin.only(left=15, top=5),
            padding=padding.only(top=10, right=15, bottom=30, left=15),
            rotate=transform.Rotate(0),
            content=self.textControl,
        )
        self.chatBlock = ListView(
                auto_scroll=True,
                height=430,
                width=0,
                controls=[
                self.interactResponse
            ]
        )

        self.mainInterface = Container(
            bgcolor="transparent",
            padding=padding.only(right=10),
            margin=margin.only(left=10,top=20),
            content=Column(
            width=710,
            controls=[
            Container(
                content=Column(
                    controls=[
                Container(
                    visible=True,
                    margin=margin.only(),
                    border=border.all(width=1, color="white"),
                    border_radius=border_radius.only(
                                top_left=20, top_right=20
                            ),
                    content=Column(
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                        Container(
                            gradient=LinearGradient(
                                begin=alignment.bottom_left,
                                end=alignment.top_right,
                                colors=["#5DE0E6", "#004AAD"],
                            ),
                            width=400,
                            height=530,
                            padding=padding.only(
                                top=10,
                                right=5,
                                bottom=10,
                                left=5,
                            ),
                            border_radius=border_radius.only(
                                top_left=20, top_right=20
                            ),
                            content=Column(
                                controls=[
                                  self.searchHead,
                                  self.searchContent
                                ]
                            ),
                        )
                        ],
                    ),
                ),
                Container(
                    content=Column(
                    controls=[
                    self.resultHead,
                    Container(
                            border_radius=border_radius.only(
                        top_left=20, top_right=20, bottom_left=20),
                            margin=margin.only(left=0,),
                        content=self.chatBlock
                    )
                    ]
                    )
                )
            ]
        ),
    ),
],
),
)

    def update_dimensions(self, width,height):
        self.mainInterface.height = height * 0.73
        if width > 400:
            self.mainInterface.width = width*0.55
        else:
            self.mainInterface.width = 300


    def config_variables(self,titre,lien,description,image_url):
        self.gt.append(titre)
        self.gl.append(lien)
        self.gd.append(description)
        self.gt.append(image_url)

    def update(self):
        self.config_variables()

    def write(self, new_text):
        speedTime = 0.02
        for char in new_text:
            self.botText.value += char
            if len(self.botText.value)> 300:
                self.textControl.height = 200
            self.botText.update()
            time.sleep(speedTime)
            lenText = len(self.botText.value)
            self.chatBlock.width = lenText*12
            if lenText <= 9 :
               self.chatBlock.width = 90
            if lenText >9:
                self.chatBlock.width = lenText*11
            if lenText > 16:
                self.chatBlock.width = lenText*9
            self.chatBlock.update()
            if self.botText.value == new_text:
                time.sleep(0.5)
                self.botText.value = ''
                self.chatBlock.width = 0
                self.botText.update()
                self.chatBlock.update()







class UserCommandblock:
    def __init__(self):

        self.userOutputWidth = 125
        self.textWidth = 50
        self.userOutputText = Text(
            value="",
            width=self.textWidth,
            size=12,
        )

        self.userOutput = Container(
            width=self.userOutputWidth,
            bgcolor="#828EA4",
            padding=padding.only(top=10, right=25, bottom=15, left=20),
            border_radius=10,
            content=Row(
                vertical_alignment="Top",
                controls=[
                    Container(
                        border=border.all(2, color="white"),
                        width=30,
                        height=30,
                        border_radius=30,
                    ),
                    self.userOutputText,
                ],
            ),
        )
        self.userCommand = Container(
            visible=True,
            width=710,
            bgcolor="transparent",
            margin=margin.only(top=10),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    self.userOutput,
                ],
            ),
        )


    def update_text(self, new_text):
        self.userOutput.visible=True
        self.userOutputText.value +=  new_text
        if len(self.userOutputText.value) < 30 :
            self.textWidth = int(7.5)*len(self.userOutputText.value)
            self.userOutputText.width = self.textWidth
            self.userOutput.width = self.userOutputWidth + 5*(len(self.userOutputText.value) - 5)
            time.sleep(0.05)
            self.userOutput.update()
            self.userOutputText.update()
        if len(self.userOutputText.value) > 30 :
            self.userOutputText.width =155
            self.userOutput.width = 236
            time.sleep(0.05)
            self.userOutput.update()
            self.userOutputText.update()
        time.sleep(3)
        self.userOutputText.value = ""
        self.userOutputText.update()
        self.userOutput.width = 125


def BgInterface_style() -> dict[str, any]:
    return {
        "expand": True,
        "margin": -10,
        "gradient": LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=["#13547a", "#13547a", "#80d0e7"],
        ),
    }


class BgInterface(Container):
    def __init__(self):
        super().__init__(**BgInterface_style())
        self.InterfaceContent = Column(controls=[])
        self.content = self.InterfaceContent


class GetText:
    def __init__(self, user_block, response_block):
        self.user_block = user_block
        self.response_block = response_block


        def voiceToText():
          try:
              with sr.Microphone() as source:
                audio = r.listen(source)
                text = r.recognize_google(audio, language='fr-FR')
                print("J'ai dit: \"{0}\"".format(text))
                self.user_block.update_text(text)
              return text.lower()
          except sr.UnknownValueError:
                print("Je n'ai pas compris ce que vous avez dit.")
          except sr.RequestError as e:
                print(f"Erreur avec le service de reconnaissance vocale : {e}")
          except Exception as e:
                print(f"Une erreur inattendue est survenue : {e}")
          return ""

        def Talk(res):
            engine.say(res)
            engine.runAndWait()

        def google_assit(command):
            api_key = 'AIzaSyDM6xiMOTDYgp-lbKw_JTXujBdGN74A_og'
            cse_id = 'c4ed8b1002da0402d'

            # Demander à l'utilisateur d'entrer une question


            # Créer une liste de sites à inclure dans la recherche
            # Exemple: "site:coding.com OR site:autresite.com"

            # Ajouter les sites à la requête
            url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={command} '

            response = requests.get(url)
            results = response.json()

            if 'items' in results:
                for item in results['items']:
                    titre = item.get("title")
                    lien = item.get("link")
                    description = item.get("snippet")
                    image_url = item.get("pagemap", {}).get("cse_image", [{}])[0].get("src", "Pas d'image disponible")

                    # Affichage des résultats dans le terminal
                    print(f'Titre: {titre}')
                    print(f'Lien: {lien}')
                    print(f'Description: {description}')
                    print(f'Image: {image_url}\n')

                    # Affichage des résultats dans le terminal
                    self.response_block.config_variables(titre,lien,description,image_url)


            else:
                print('Aucun résultat trouvé.')


        def analysing():
            command = voiceToText()
            if 'bonjour' in command:
                response= "oui! Bonjour comment tu vas"
                self.response_block.write(response)
            elif 'et toi' in command:
                print("Bixby: Je me porte à merveille")
                self.response_block.write("Je me porte à merveille")
                #Talk(response)
            elif 'la plus belle au monde' in command:
                google_assit(command)



        while True:
            text = voiceToText()
            if text != 0:
               analysing()


def main(page: Page) -> None:
    page.title = "Bixby"
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.theme_mode = ThemeMode.DARK
    page.window_max_height = 720
    page.window_max_width = 700

    # Instances

    response_block = mainInterface(page)
    user_block = UserCommandblock()
    bground = BgInterface()
    bground.InterfaceContent.controls.extend(
        [
            user_block.userCommand,
            response_block.mainInterface,
            #botHouse().botHouse,
        ]
    )

    # Initial size update
    response_block.update_dimensions(page.window_width,page.window_height)

    # Handle resize event
    def on_resize(e):
        response_block.update_dimensions(page.window_width,page.window_height)
        page.update()

    page.on_resize = on_resize
    page.add(bground)

    # Lancer la génération de texte

    generate_text = GetText( user_block,response_block)
    generate_text.voiceToText()

  

if __name__ == "__main__":
    flet.app(target=main)
