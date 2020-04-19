import os
import webbrowser
import json
import requests
import time
from time import sleep
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager,Screen,SlideTransition
from kivy.uix.image import Image
from kivy.garden.navigationdrawer import NavigationDrawer as ND
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.checkbox import CheckBox
from kivy.garden.mapview import MapView,MapMarker,MapSource
from kivy.core.window import Window

class About(Screen):
    def go_home(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'home'
 
class ChangePassword(Screen):
    def change(self,uid,ied):
        usname=self.manager.get_screen('forgotpassword').ids['uid'].text
        if uid==ied:
            url = 'https://busio-f6319.firebaseio.com/.json'
            auth_key = 'wUF3L7q57MPvrFYQ69ojsIivBPcGwAFs4b8Vi4HG' 
            request = requests.get(url + '?auth=' + auth_key)
            p=request.json()
            j=p["Login"]
            a=j[str(usname)]
            a["Password"]=uid
            JSON=json.dumps(a)
            to_database = json.loads(JSON)
            requests.patch(url = url[:-5]+"Login/"+str(usname)+"/.json", json = to_database)
            self.manager.transition = SlideTransition(direction="right")
            self.manager.current = 'home'

class VerifyOTP(Screen):
    def verify(self,otp):
        real_otp=self.manager.get_screen('forgotpassword').otp
        #print(real_otp,otp)
        if real_otp==otp:
            self.manager.transition = SlideTransition(direction="right")
            self.manager.current = 'changepassword'
        else:
            print('Wrong otp')

    def go_forgotpassword(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'forgotpassword'

class ForgotPassword(Screen):
    otp=None
    def sendotp(self,uid):
        import emis
        url = 'https://busio-f6319.firebaseio.com/.json'
        auth_key = 'wUF3L7q57MPvrFYQ69ojsIivBPcGwAFs4b8Vi4HG' 
        request = requests.get(url + '?auth=' + auth_key)
        p=request.json() 
        if uid in p["Login"]:
            self.otp=emis.sendmail(p["Login"][uid]["Email"])
            self.manager.transition = SlideTransition(direction="right")
            self.manager.current = 'verify'
        else:
            self.ids['err'].text='Username doesn\'t exists'
    
    def go_login(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'   
        
class CustomDropDown(DropDown):
    pass
    
class HomeND(Screen):
    dropdown = CustomDropDown()
    mainbutton = Button(text='Hello', size_hint=(None, None))
    mainbutton.bind(on_release=dropdown.open)
    dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
    url = 'https://busio-f6319.firebaseio.com/.json' # You must add .json to the end of the URL
    auth_key = 'wUF3L7q57MPvrFYQ69ojsIivBPcGwAFs4b8Vi4HG' # Refer to the YouTube video on where to find this.
   
    def on_enter(self):
        from gmd import short_dist
        dist=short_dist('Bhopal Chouraha','Mahakal Institute Of Technology')
        self.ids['dis'].text=dist
    def go_about(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'about'
        

    def logout(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()
    
    def on_checkbox_active(self, value):
        #print(value)
        if value=="Dewas":
            self.latitude = 22.962267
            self.longitude = 76.050797
            self.ids.mv.center_on(self.latitude, self.longitude)
            self.ids.mv.zoom=11
            #source = MapSource(url="map11.html",cache_key="my-custom-map", tile_size=512,image_ext="png", attribution="@ Myself")
            #self.ids.mv.map_source = source
            for i in range(1):
                request = requests.get(self.url + '?auth=' + self.auth_key)
                p=request.json()
                a=p["Dewas"]
                #print(a)
                for i,e in a.items():
                    la=e["lat"]
                    lo=e["lon"]
                    m=MapMarker(lon=lo,lat=la)
                    self.ids.mv.add_marker(m)
            for i in range(5):
                time.sleep(5)
                la=22.962267+i*0.1
                lo=76.050797+i*0.1
                m=MapMarker(lon=lo,lat=la,size_hint=(50,50),anchor_x=0.2,anchor_y=0.2,source=r"images\busicon.png")
                self.ids.mv.add_marker(m)
    
        elif value=="Ujjain":
            self.latitude = 23.18239
            self.longitude =  75.77643
            self.ids.mv.center_on(self.latitude, self.longitude)
            self.ids.mv.zoom=11
            for i in range(1):
                request = requests.get(self.url + '?auth=' + self.auth_key)
                p=request.json()
                a=p["Ujjain"]

class Login(Screen):
    url = 'https://busio-f6319.firebaseio.com/.json'
    auth_key = 'wUF3L7q57MPvrFYQ69ojsIivBPcGwAFs4b8Vi4HG' # Refer to the YouTube video on where to find this.
 
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()
        request = requests.get(self.url + '?auth=' + self.auth_key)
        p=request.json()
    
        app.username = loginText
        app.password = passwordText
        #print(app.username,app.password)
  
        if app.username in p["Login"]:
            if app.password==p["Login"][app.username]["Password"]:
                if app.username=='0704CS171024' or app.username=='0704CS171018' or app.username=='0704ADMIN2019':
                    self.manager.transition=SlideTransition(direction="right")
                    self.manager.current='Admin'
                else:      
                    self.ids['err'].text="" 
                    self.manager.transition = SlideTransition(direction="left")
                    self.manager.current = 'home'
            else:
                self.ids['err'].text="Wrong Password"
        else:
            self.ids['err'].text="Wrong Username"

        app.config.read(app.get_application_config())
        app.config.write()

    def forgot_password(self):
         self.manager.transition = SlideTransition(direction="right")
         self.manager.current = 'forgotpassword'

    def resetForm(self):
        self.ids['login'].text = "Username"
        self.ids['password'].text = "Password"
        
class ManageAdmin(Screen):
    pass
    def Add(self,a,c,d):
        url = 'https://busio-f6319.firebaseio.com/.json'
        auth_key = 'wUF3L7q57MPvrFYQ69ojsIivBPcGwAFs4b8Vi4HG'
        JSON={}
        JSON[str(a)]={'Email':c,'Password':d}
        print(JSON)
        JSON=json.dumps(JSON)
        to_database = json.loads(JSON)
        requests.patch(url = url[:-5]+"Login/.json", json = to_database)
        print("Add/Update operation successful")
    def Del(self,a,c,d):
        url = 'https://busio-f6319.firebaseio.com/.json'
        auth_key = 'wUF3L7q57MPvrFYQ69ojsIivBPcGwAFs4b8Vi4HG'
        JSON={}
        JSON[str(a)]={'Email':c,'Password':d}
        requests.delete(url = url[:-5]+"Login/" + str(a) + ".json")
        print("Delete operation successful")
    def go_login(self):
        self.manager.transition=SlideTransition(direction="left")
        self.manager.current='Admin'
          
          
class AdminScreen(Screen):
    def GoManage(self):
        self.manager.transition=SlideTransition(direction="left")
        self.manager.current='Manage'
    def GoTrack(self):
        self.manager.transition=SlideTransition(direction="left")
        self.manager.current='home'
    def GoBack(self):
        self.manager.transition=SlideTransition(direction="left")
        self.manager.current='login'
          
          
          

class Welcome(Screen):
    def do_change(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'login'
   
class BusIO(App):
    
    def build(self):
        manager = ScreenManager()
        manager.add_widget(Welcome(name='welcome'))
        login=Login(name='login')
        button = Button(pos=(0,-20),size_hint=(None, None),background_normal=r"images\sch.png",on_press =self.animate)
        login.add_widget(button)
        login.bind(on_enter=self.click)
        manager.add_widget(login)
        manager.add_widget(HomeND(name='home'))
        manager.add_widget(ForgotPassword(name='forgotpassword'))
        manager.add_widget(VerifyOTP(name='verify'))
        manager.add_widget(ChangePassword(name='changepassword'))
        manager.add_widget(About(name='about'))
        manager.add_widget(AdminScreen(name='Admin'))
        manager.add_widget(ManageAdmin(name='Manage'))

        return manager
     
    def get_application_config(self):
        if(not self.username):
            return super(BusIO, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(BusIO, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )

    def animate(self, instance):
        # create an animation object. This object could be stored
        # and reused each call or reused across different widgets.
        # += is a sequential step, while &= is in parallel
        #print("hello")
        animation = Animation(pos=(instance.parent.width-500, -20),duration=3.)
        animation =animation+ Animation(pos=(0, -20),duration=3.)

        # apply the animation on the button, passed in the "instance" argument
        # Notice that default 'click' animation (changing the button
        # color while the mouse is down) is unchanged.
        animation.repeat=True
        animation.start(instance)
        
    def click(self,instance):
        #print(instance.children)
        instance.children[0].trigger_action()
        
if __name__=="__main__":
  LabelBase.register(name="Broadway",fn_regular="fonts/BroadwayFlat.ttf")
  LabelBase.register(name="Baskerville",fn_regular="fonts/BaskervilleBoldfont.ttf")
  LabelBase.register(name="BodoniFLF-Bold",fn_regular="fonts/BodoniFLF-Bold.ttf")
  LabelBase.register(name="arb",fn_regular="fonts/ArialRoundedBold.ttf")
  LabelBase.register(name="crimson",fn_regular="fonts/Crimson-Roman.ttf")
  LabelBase.register(name="ComicSansMS3",fn_regular="fonts/comicz.ttf")
  LabelBase.register(name="brush",fn_regular="fonts/BRUSHSCI.ttf")
  BusIO().run()



