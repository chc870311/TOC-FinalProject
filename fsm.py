from transitions.extensions import GraphMachine

from utils import send_text_message,send_image
import random

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "0"
    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "1"
    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "2"
    def is_going_to_state4(self, event):
        text = event.message.text
        return text.lower() == "3"
    
    def is_going_to_state5(self, event):
        text = event.message.text
        return text.lower() == "0"
    def is_going_to_state6(self, event):
        text = event.message.text
        return text.lower() == "1"
    def is_going_to_state7(self, event):
        text = event.message.text
        return text.lower() == "2"
    
    def is_going_to_state8(self, event):
        text = event.message.text
        return text.lower() == "0"
    def is_going_to_state9(self, event):
        text = event.message.text
        return text.lower() == "1"
    def is_going_to_state10(self, event):
        text = event.message.text
        return text.lower() == "2"
    
    def is_going_to_state11(self, event):
        text = event.message.text
        return text.lower() == "0"
    def is_going_to_state12(self, event):
        text = event.message.text
        return text.lower() == "1"
    def is_going_to_state13(self, event):
        text = event.message.text
        return text.lower() == "2"
    
    def is_going_to_state14(self, event):
        text = event.message.text
        return text.lower() == "0"
    def is_going_to_state15(self, event):
        text = event.message.text
        return text.lower() == "1"
    def is_going_to_state16(self, event):
        text = event.message.text
        return text.lower() == "2"
    
    def is_going_to_show_fsm(self, event):
        text = event.message.text
        return text.lower() == "show_fsm"
    
		
    def on_enter_state1(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "飯")
        
    def on_enter_state2(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token,"麵")
        
    def on_enter_state3(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "其他")
        
    def on_enter_state4(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "隨便")
    
    def on_enter_state5(self, event):
        reply_token = event.reply_token
        a = random.randint(1,6)
        if a==1:
            send_text_message(reply_token, "成大館\nhttps://www.google.com/maps/place/%E6%88%90%E5%A4%A7%E9%A4%A8/@22.9953792,120.2171415,21z/data=!4m5!3m4!1s0x346e76926469f5db:0x63ca5caef2bcb5dd!8m2!3d22.9955252!4d120.2171113")
        elif a==2:
            send_text_message(reply_token, "奧莉薇\nhttps://www.google.com/maps/place/%E5%A5%A7%E8%8E%89%E8%96%87%E7%94%9F%E6%B4%BB%E5%BB%9A%E6%88%BF/@22.9954225,120.2168617,21z/data=!4m5!3m4!1s0x346e76927a4ef149:0xd009b021604b439d!8m2!3d22.995369!4d120.2169165")
        elif a==3:
            send_text_message(reply_token, "上樂炒飯\nhttps://www.google.com/maps/place/%E4%B8%8A%E6%A8%82%E7%82%92%E9%A3%AF%E5%B0%88%E8%B3%A3%E5%BA%97/@22.9954575,120.2160394,21z/data=!4m5!3m4!1s0x346e768d8435fcd9:0xcc114221cc54fac6!8m2!3d22.9954369!4d120.2161353")
        elif a==4:
            send_text_message(reply_token, "勝早\nhttps://www.google.com/maps/place/%E5%8B%9D%E5%88%A9%E6%97%A9%E9%BB%9E/@22.9946876,120.217469,20.75z/data=!4m5!3m4!1s0x346e76926a16a7bb:0xc12e2e860b5f50b1!8m2!3d22.9946561!4d120.2179156")
        elif a==5:
            send_text_message(reply_token, "光復學餐\nhttps://www.google.com/maps/place/%E5%85%AB%E6%96%B9%E9%9B%B2%E9%9B%86+%E5%8F%B0%E5%8D%97%E6%88%90%E5%A4%A7%E5%BA%97(%E5%85%89%E5%BE%A9%E6%A0%A1%E5%8D%80%E5%AD%B8%E7%94%9F%E9%A4%90%E5%BB%B3%EF%BC%89/@22.9992439,120.2150734,18.75z/data=!4m5!3m4!1s0x346e773e2fd35991:0x4ab86daf208974b2!8m2!3d22.9991522!4d120.2150356")
        elif a==6:
            send_text_message(reply_token, "活力小廚\nhttps://www.google.com/maps/place/%E6%B4%BB%E5%8A%9B%E5%B0%8F%E5%BB%9A/@22.9958538,120.2168351,20z/data=!4m5!3m4!1s0x0:0xdf9bf73d06971751!8m2!3d22.995645!4d120.216851")
        self.go_back()
    def on_enter_state6(self, event):
        reply_token = event.reply_token
        a = random.randint(1,4)
        if a==1:
            send_text_message(reply_token, "鹿杯\nhttps://www.google.com/maps/place/%E9%B9%BF%E6%9D%AF%E9%A3%B2%E9%A3%9F/@22.9954393,120.2150773,20.5z/data=!4m5!3m4!1s0x346e77dfbfca3d79:0x10449cb78707db61!8m2!3d22.9956635!4d120.2150812")
        elif a==2:
            send_text_message(reply_token, "樂品屋\nhttps://www.google.com/maps/place/%E6%A8%82%E5%93%81%E5%B1%8B/@22.9951398,120.2147686,21z/data=!4m5!3m4!1s0x346e768dbf510fa1:0x39d210b07df2f5fe!8m2!3d22.9949406!4d120.2146943")
        elif a==3:
            send_text_message(reply_token, "雙城烤雞\nhttps://www.google.com/maps/place/%E9%9B%99%E5%9F%8E%E7%83%A4%E9%9B%9E%E9%A3%AF/@22.9951398,120.2147686,21z/data=!4m5!3m4!1s0x346e768dbf6414bd:0xac6810360eb1694f!8m2!3d22.994919!4d120.2148499")
        elif a==4:
            send_text_message(reply_token, "紅樓小館\nhttps://www.google.com/maps/place/%E7%B4%85%E6%A8%93%E5%B0%8F%E9%A4%A8/@22.9958538,120.2168351,20z/data=!4m5!3m4!1s0x346e769aa810d523:0xfe05d2e87fce4b97!8m2!3d22.9958418!4d120.2170318")
        self.go_back()
    def on_enter_state7(self, event):
        reply_token = event.reply_token
        a = random.randint(1,2)
        if a==1:
            send_text_message(reply_token, "豚讚豬排\nhttps://www.google.com/maps/place/%E8%B1%9A%E8%AE%9A%E6%97%A5%E5%BC%8F%E8%B1%AC%E6%8E%92/@22.9917343,120.2176687,19.5z/data=!4m12!1m6!3m5!1s0x346e76938c3a29cd:0xad41338d70f56c8f!2z5Zub5rW36YGK6b6N6Y2L6LK85bCI6LOj5bqXIC0g5Y-w5Y2X6ZW35qau5bqX!8m2!3d22.9937993!4d120.2218518!3m4!1s0x346e7691eb7ea5bd:0x29a2c10c826f02f3!8m2!3d22.9920752!4d120.2179056")
        elif a==2:
            send_text_message(reply_token, "元味屋\nhttps://www.google.com/maps/place/%E5%85%83%E5%91%B3%E5%B1%8B%E5%92%8C%E9%A2%A8%E6%B4%8B%E9%A3%9F/@22.9942822,120.2152823,18.25z/data=!4m12!1m6!3m5!1s0x346e76938c3a29cd:0xad41338d70f56c8f!2z5Zub5rW36YGK6b6N6Y2L6LK85bCI6LOj5bqXIC0g5Y-w5Y2X6ZW35qau5bqX!8m2!3d22.9937993!4d120.2218518!3m4!1s0x346e768db909a2c9:0x258b2672fc2a431e!8m2!3d22.995282!4d120.2146259")
        self.go_back()
    def on_enter_state8(self, event):
        reply_token = event.reply_token
        a = random.randint(1,4)
        if a==1:
            send_text_message(reply_token, "來碗拉麵\nhttps://www.google.com/maps/place/%E4%BE%86%E7%A2%97%E6%8B%89%E9%BA%B5+%E8%82%B2%E6%A8%82%E5%BA%97/@22.9955837,120.2156768,21z/data=!4m12!1m6!3m5!1s0x346e76938c3a29cd:0xad41338d70f56c8f!2z5Zub5rW36YGK6b6N6Y2L6LK85bCI6LOj5bqXIC0g5Y-w5Y2X6ZW35qau5bqX!8m2!3d22.9937993!4d120.2218518!3m4!1s0x346e768d9a43e715:0x2bf723ac09cb4959!8m2!3d22.9955937!4d120.2156847")
        elif a==2:
            send_text_message(reply_token, "御鍋燒\nhttps://www.google.com/maps/place/%E5%BE%A1%E9%8D%8B%E7%87%92/@22.9955506,120.2158723,21z/data=!4m12!1m6!3m5!1s0x346e76938c3a29cd:0xad41338d70f56c8f!2z5Zub5rW36YGK6b6N6Y2L6LK85bCI6LOj5bqXIC0g5Y-w5Y2X6ZW35qau5bqX!8m2!3d22.9937993!4d120.2218518!3m4!1s0x346e7752b5de3ced:0xfd5ccad3e0f05ddc!8m2!3d22.9955116!4d120.2159509")
        elif a==3:
            send_text_message(reply_token, "九州拉麵\nhttps://www.google.com/maps/place/%E4%B9%9D%E5%B7%9E%E8%B1%9A%E9%AA%A8%E6%8B%89%E9%BA%B5/@22.995476,120.2176174,21z/data=!4m12!1m6!3m5!1s0x346e76938c3a29cd:0xad41338d70f56c8f!2z5Zub5rW36YGK6b6N6Y2L6LK85bCI6LOj5bqXIC0g5Y-w5Y2X6ZW35qau5bqX!8m2!3d22.9937993!4d120.2218518!3m4!1s0x346e76926397301f:0x474ded1ae94caba6!8m2!3d22.995532!4d120.2175871")
        elif a==4:
            send_text_message(reply_token, "yes58義大利麵\nhttps://www.google.com/maps/place/yes58%E7%BE%A9%E5%A4%A7%E5%88%A9%E9%BA%B5/@22.9954318,120.2170195,21z/data=!4m12!1m6!3m5!1s0x346e76938c3a29cd:0xad41338d70f56c8f!2z5Zub5rW36YGK6b6N6Y2L6LK85bCI6LOj5bqXIC0g5Y-w5Y2X6ZW35qau5bqX!8m2!3d22.9937993!4d120.2218518!3m4!1s0x346e7692649730ef:0xb415aa92d6f8c1ca!8m2!3d22.9954036!4d120.2174838")
        self.go_back()
    def on_enter_state9(self, event):
        reply_token = event.reply_token
        a = random.randint(1,2)
        if a==1:
            send_text_message(reply_token, "大醬麵館\nhttps://www.google.com/maps/place/%E5%A4%A7%E9%86%AC%E5%B7%9D%E9%BA%B5%E9%A4%A8/@22.9954978,120.2169313,21z/data=!4m5!3m4!1s0x346e7692797924ad:0xb0aca00082132df0!8m2!3d22.9954017!4d120.2169862")
        elif a==2:
            send_text_message(reply_token, "好煮義\nhttps://www.google.com/maps/place/%E5%A5%BD%E7%85%AE%E7%BE%A9%E7%BE%A9%E5%A4%A7%E5%88%A9%E9%BA%B5/@22.9949907,120.214856,21z/data=!4m5!3m4!1s0x346e768dc793db25:0x1e0119060e1b497b!8m2!3d22.9949968!4d120.2146983")
        self.go_back()
    def on_enter_state10(self, event):
        reply_token = event.reply_token
        a = random.randint(1,3)
        if a==1:
            send_text_message(reply_token, "Mr.拉麵\nhttps://www.google.com/maps/place/Mr.%E6%8B%89%E9%BA%B5(%E5%8F%B0%E5%8D%97%E5%BA%97)/@22.9921526,120.2175339,19z/data=!4m5!3m4!1s0x346e7691c037aa79:0xb30c14ea40fa2239!8m2!3d22.9916221!4d120.2178533")
        elif a==2:
            send_text_message(reply_token, "老夫子牛肉麵\nhttps://www.google.com/maps/place/%E8%82%B2%E6%A8%82%E8%A1%97%E8%80%81%E5%A4%AB%E5%AD%90%E7%89%9B%E8%82%89%E9%BA%B5/@22.9939093,120.2147871,19z/data=!4m5!3m4!1s0x346e768dc705d7b9:0x36e2d592127c9cb9!8m2!3d22.9945536!4d120.2145555")
        elif a==3:
            send_text_message(reply_token, "江南美食\nhttps://www.google.com/maps/place/%E6%B1%9F%E5%8D%97%E7%BE%8E%E9%A3%9F+%E9%BB%83%E7%89%9B%E8%82%89%E9%BA%B5(%E5%8F%B0%E5%8D%97%E8%82%B2%E6%A8%82%E5%BA%97)/@22.9947943,120.2151654,19z/data=!4m5!3m4!1s0x0:0x42e6eb4e5997a6c6!8m2!3d22.9949457!4d120.2148123")
        self.go_back()
    def on_enter_state11(self, event):
        reply_token = event.reply_token
        a = random.randint(1,4)
        if a==1:
            send_text_message(reply_token, "加依軒\nhttps://www.google.com/maps/place/%E5%8A%A0%E4%BE%9D%E8%BB%92%EF%BC%88%2B1%EF%BC%89%E5%B0%8F%E7%B1%A0%E6%B9%AF%E5%8C%85%E6%88%90%E5%A4%A7%E5%BA%97/@22.9953082,120.2170482,21z/data=!4m5!3m4!1s0x346e76927bffb2a9:0x520c3de4baf20ad5!8m2!3d22.9955295!4d120.2170385")
        elif a==2:
            send_text_message(reply_token, "小上海香酥雞\nhttps://www.google.com/maps/place/%E5%B0%8F%E4%B8%8A%E6%B5%B7%E9%A6%99%E9%85%A5%E9%9B%9E/@22.99549,120.2167448,21z/data=!4m5!3m4!1s0x346e768d9b374391:0xfb0fc906207123d2!8m2!3d22.9954739!4d120.2169688")
        elif a==3:
            send_text_message(reply_token, "派克雞排\nhttps://www.google.com/maps/place/2%E6%B4%BE%E5%85%8B%E8%84%86%E7%9A%AE%E9%9B%9E%E6%8E%92/@22.99549,120.2167448,21z/data=!4m5!3m4!1s0x346e768d87309b29:0x1a25026f887ae8b3!8m2!3d22.9956443!4d120.2168515")
        elif a==4:
            send_text_message(reply_token, "四海遊龍\nhttps://www.google.com/maps/place/%E5%9B%9B%E6%B5%B7%E9%81%8A%E9%BE%8D%E9%8D%8B%E8%B2%BC%E5%B0%88%E8%B3%A3%E5%BA%97+-+%E5%8F%B0%E5%8D%97%E9%95%B7%E6%A6%AE%E5%BA%97/@22.9939161,120.2217388,18.75z/data=!4m5!3m4!1s0x346e76938c3a29cd:0xad41338d70f56c8f!8m2!3d22.9937993!4d120.2218518")
        self.go_back()
    def on_enter_state12(self, event):
        reply_token = event.reply_token
        a = random.randint(1,4)
        if a==1:
            send_text_message(reply_token, "惡魔雞排\nhttps://www.google.com/maps/place/%E5%89%B5%E5%A7%8B%E6%83%A1%E9%AD%94%E9%9B%9E%E6%8E%92%E2%80%94%E5%8F%B0%E5%8D%97%E8%82%B2%E6%A8%82%E5%BA%97/@22.9955145,120.2165546,21z/data=!4m5!3m4!1s0x346e770cd6339c13:0xa8204866ab851018!8m2!3d22.9955425!4d120.2165423")
        elif a==2:
            send_text_message(reply_token, "大夯牛排\nhttps://www.google.com/maps/place/%E5%A4%A7%E5%A4%AF%E7%89%9B%E6%8E%92%E9%A4%A8Da-hang+Steak+house/@22.9953082,120.2170482,21z/data=!4m5!3m4!1s0x346e76927bb78707:0xcca908f72b7a20cd!8m2!3d22.9954042!4d120.2171123")
        elif a==3:
            send_text_message(reply_token, "品都炭烤\nhttps://www.google.com/maps/place/%E5%93%81%E9%83%BD%E7%87%92%E7%83%A4+%E6%88%90%E5%A4%A7%E5%BA%97/@22.9955145,120.2165546,21z/data=!4m5!3m4!1s0x346e768d8774afc7:0xbf070f580153bac3!8m2!3d22.9954962!4d120.2165638")
        elif a==4:
            send_text_message(reply_token, "小赤佬\nhttps://www.google.com/maps/place/%E5%B0%8F%E8%B5%A4%E4%BD%AC%E5%B9%B2%E9%8D%8B+%E8%82%B2%E6%A8%82%E5%BA%97/@22.9954169,120.2173373,21z/data=!4m5!3m4!1s0x346e769264b112d7:0xc618979fe2c749d8!8m2!3d22.9954141!4d120.2174013")
        self.go_back()
    def on_enter_state13(self, event):
        reply_token = event.reply_token
        a = random.randint(1,4)
        if a==1:
            send_text_message(reply_token, "麥當勞\nhttps://www.google.com/maps/place/%E9%BA%A5%E7%95%B6%E5%8B%9E-%E5%8F%B0%E5%8D%97%E5%A4%A7%E5%AD%B8%E5%BA%97/@22.9957039,120.2206845,19.25z/data=!4m5!3m4!1s0x346e76936e9b3923:0x8d9e313cba2f84e6!8m2!3d22.9959529!4d120.221369")
        elif a==2:
            send_text_message(reply_token, "肯德基\nhttps://www.google.com/maps/place/%E8%82%AF%E5%BE%B7%E5%9F%BAKFC-%E5%8F%B0%E5%8D%97%E6%88%90%E5%A4%A7%E9%A4%90%E5%BB%B3/@22.9957039,120.2206845,19.25z/data=!4m5!3m4!1s0x346e7693132530db:0xe63489d34fe26cf2!8m2!3d22.9959455!4d120.2209277")
        elif a==3:
            send_text_message(reply_token, "21風味館\nhttps://www.google.com/maps/place/21%E9%A2%A8%E5%91%B3%E9%A4%A8+%E5%8F%B0%E5%8D%97%E6%88%90%E5%A4%A7%E9%96%80%E5%B8%82/@22.9957468,120.2189054,19.25z/data=!4m5!3m4!1s0x0:0xf6abbaf32358f41a!8m2!3d22.9957758!4d120.2182787")
        elif a==4:
            send_text_message(reply_token, "哞王\nhttps://www.google.com/maps/place/%E5%93%9E%E7%8E%8B%E5%8E%9F%E5%91%B3%E7%82%AD%E7%83%A4%E7%89%9B%E6%8E%92/@22.995539,120.2151452,19.25z/data=!4m5!3m4!1s0x346e768d9a7f30c7:0x25ab2e268ce12e33!8m2!3d22.9954906!4d120.2157303")
        self.go_back()
    def on_enter_state14(self, event):
        reply_token = event.reply_token
        a = random.randint(1,14)
        if a==1:
            send_text_message(reply_token, "成大館\nhttps://www.google.com/maps/place/%E6%88%90%E5%A4%A7%E9%A4%A8/@22.9953792,120.2171415,21z/data=!4m5!3m4!1s0x346e76926469f5db:0x63ca5caef2bcb5dd!8m2!3d22.9955252!4d120.2171113")
        elif a==2:
            send_text_message(reply_token, "奧莉薇\nhttps://www.google.com/maps/place/%E5%A5%A7%E8%8E%89%E8%96%87%E7%94%9F%E6%B4%BB%E5%BB%9A%E6%88%BF/@22.9954225,120.2168617,21z/data=!4m5!3m4!1s0x346e76927a4ef149:0xd009b021604b439d!8m2!3d22.995369!4d120.2169165")
        elif a==3:
            send_text_message(reply_token, "上樂炒飯\nhttps://www.google.com/maps/place/%E4%B8%8A%E6%A8%82%E7%82%92%E9%A3%AF%E5%B0%88%E8%B3%A3%E5%BA%97/@22.9954575,120.2160394,21z/data=!4m5!3m4!1s0x346e768d8435fcd9:0xcc114221cc54fac6!8m2!3d22.9954369!4d120.2161353")
        elif a==4:
            send_text_message(reply_token, "勝早\nhttps://www.google.com/maps/place/%E5%8B%9D%E5%88%A9%E6%97%A9%E9%BB%9E/@22.9946876,120.217469,20.75z/data=!4m5!3m4!1s0x346e76926a16a7bb:0xc12e2e860b5f50b1!8m2!3d22.9946561!4d120.2179156")
        elif a==5:
            send_text_message(reply_token, "光復學餐\nhttps://www.google.com/maps/place/%E5%85%AB%E6%96%B9%E9%9B%B2%E9%9B%86+%E5%8F%B0%E5%8D%97%E6%88%90%E5%A4%A7%E5%BA%97(%E5%85%89%E5%BE%A9%E6%A0%A1%E5%8D%80%E5%AD%B8%E7%94%9F%E9%A4%90%E5%BB%B3%EF%BC%89/@22.9992439,120.2150734,18.75z/data=!4m5!3m4!1s0x346e773e2fd35991:0x4ab86daf208974b2!8m2!3d22.9991522!4d120.2150356")
        elif a==6:
            send_text_message(reply_token, "活力小廚\nhttps://www.google.com/maps/place/%E6%B4%BB%E5%8A%9B%E5%B0%8F%E5%BB%9A/@22.9958538,120.2168351,20z/data=!4m5!3m4!1s0x0:0xdf9bf73d06971751!8m2!3d22.995645!4d120.216851")
        elif a==7:
            send_text_message(reply_token, "來碗拉麵\nhttps://www.google.com/maps/place/%E4%BE%86%E7%A2%97%E6%8B%89%E9%BA%B5+%E8%82%B2%E6%A8%82%E5%BA%97/@22.9955837,120.2156768,21z/data=!4m12!1m6!3m5!1s0x346e76938c3a29cd:0xad41338d70f56c8f!2z5Zub5rW36YGK6b6N6Y2L6LK85bCI6LOj5bqXIC0g5Y-w5Y2X6ZW35qau5bqX!8m2!3d22.9937993!4d120.2218518!3m4!1s0x346e768d9a43e715:0x2bf723ac09cb4959!8m2!3d22.9955937!4d120.2156847")
        elif a==8:
            send_text_message(reply_token, "御鍋燒\nhttps://www.google.com/maps/place/%E5%BE%A1%E9%8D%8B%E7%87%92/@22.9955506,120.2158723,21z/data=!4m12!1m6!3m5!1s0x346e76938c3a29cd:0xad41338d70f56c8f!2z5Zub5rW36YGK6b6N6Y2L6LK85bCI6LOj5bqXIC0g5Y-w5Y2X6ZW35qau5bqX!8m2!3d22.9937993!4d120.2218518!3m4!1s0x346e7752b5de3ced:0xfd5ccad3e0f05ddc!8m2!3d22.9955116!4d120.2159509")
        elif a==9:
            send_text_message(reply_token, "九州拉麵\nhttps://www.google.com/maps/place/%E4%B9%9D%E5%B7%9E%E8%B1%9A%E9%AA%A8%E6%8B%89%E9%BA%B5/@22.995476,120.2176174,21z/data=!4m12!1m6!3m5!1s0x346e76938c3a29cd:0xad41338d70f56c8f!2z5Zub5rW36YGK6b6N6Y2L6LK85bCI6LOj5bqXIC0g5Y-w5Y2X6ZW35qau5bqX!8m2!3d22.9937993!4d120.2218518!3m4!1s0x346e76926397301f:0x474ded1ae94caba6!8m2!3d22.995532!4d120.2175871")
        elif a==10:
            send_text_message(reply_token, "yes58義大利麵\nhttps://www.google.com/maps/place/yes58%E7%BE%A9%E5%A4%A7%E5%88%A9%E9%BA%B5/@22.9954318,120.2170195,21z/data=!4m12!1m6!3m5!1s0x346e76938c3a29cd:0xad41338d70f56c8f!2z5Zub5rW36YGK6b6N6Y2L6LK85bCI6LOj5bqXIC0g5Y-w5Y2X6ZW35qau5bqX!8m2!3d22.9937993!4d120.2218518!3m4!1s0x346e7692649730ef:0xb415aa92d6f8c1ca!8m2!3d22.9954036!4d120.2174838")
        elif a==11:
            send_text_message(reply_token, "加依軒\nhttps://www.google.com/maps/place/%E5%8A%A0%E4%BE%9D%E8%BB%92%EF%BC%88%2B1%EF%BC%89%E5%B0%8F%E7%B1%A0%E6%B9%AF%E5%8C%85%E6%88%90%E5%A4%A7%E5%BA%97/@22.9953082,120.2170482,21z/data=!4m5!3m4!1s0x346e76927bffb2a9:0x520c3de4baf20ad5!8m2!3d22.9955295!4d120.2170385")
        elif a==12:
            send_text_message(reply_token, "小上海香酥雞\nhttps://www.google.com/maps/place/%E5%B0%8F%E4%B8%8A%E6%B5%B7%E9%A6%99%E9%85%A5%E9%9B%9E/@22.99549,120.2167448,21z/data=!4m5!3m4!1s0x346e768d9b374391:0xfb0fc906207123d2!8m2!3d22.9954739!4d120.2169688")
        elif a==13:
            send_text_message(reply_token, "派克雞排\nhttps://www.google.com/maps/place/2%E6%B4%BE%E5%85%8B%E8%84%86%E7%9A%AE%E9%9B%9E%E6%8E%92/@22.99549,120.2167448,21z/data=!4m5!3m4!1s0x346e768d87309b29:0x1a25026f887ae8b3!8m2!3d22.9956443!4d120.2168515")
        elif a==14:
            send_text_message(reply_token, "四海遊龍\nhttps://www.google.com/maps/place/%E5%9B%9B%E6%B5%B7%E9%81%8A%E9%BE%8D%E9%8D%8B%E8%B2%BC%E5%B0%88%E8%B3%A3%E5%BA%97+-+%E5%8F%B0%E5%8D%97%E9%95%B7%E6%A6%AE%E5%BA%97/@22.9939161,120.2217388,18.75z/data=!4m5!3m4!1s0x346e76938c3a29cd:0xad41338d70f56c8f!8m2!3d22.9937993!4d120.2218518")
        self.go_back()
    def on_enter_state15(self, event):
        reply_token = event.reply_token
        a = random.randint(1,10)
        if a==1:
            send_text_message(reply_token, "鹿杯\nhttps://www.google.com/maps/place/%E9%B9%BF%E6%9D%AF%E9%A3%B2%E9%A3%9F/@22.9954393,120.2150773,20.5z/data=!4m5!3m4!1s0x346e77dfbfca3d79:0x10449cb78707db61!8m2!3d22.9956635!4d120.2150812")
        elif a==2:
            send_text_message(reply_token, "樂品屋\nhttps://www.google.com/maps/place/%E6%A8%82%E5%93%81%E5%B1%8B/@22.9951398,120.2147686,21z/data=!4m5!3m4!1s0x346e768dbf510fa1:0x39d210b07df2f5fe!8m2!3d22.9949406!4d120.2146943")
        elif a==3:
            send_text_message(reply_token, "雙城烤雞\nhttps://www.google.com/maps/place/%E9%9B%99%E5%9F%8E%E7%83%A4%E9%9B%9E%E9%A3%AF/@22.9951398,120.2147686,21z/data=!4m5!3m4!1s0x346e768dbf6414bd:0xac6810360eb1694f!8m2!3d22.994919!4d120.2148499")
        elif a==4:
            send_text_message(reply_token, "紅樓小館\nhttps://www.google.com/maps/place/%E7%B4%85%E6%A8%93%E5%B0%8F%E9%A4%A8/@22.9958538,120.2168351,20z/data=!4m5!3m4!1s0x346e769aa810d523:0xfe05d2e87fce4b97!8m2!3d22.9958418!4d120.2170318")
        elif a==5:
            send_text_message(reply_token, "大醬麵館\nhttps://www.google.com/maps/place/%E5%A4%A7%E9%86%AC%E5%B7%9D%E9%BA%B5%E9%A4%A8/@22.9954978,120.2169313,21z/data=!4m5!3m4!1s0x346e7692797924ad:0xb0aca00082132df0!8m2!3d22.9954017!4d120.2169862")
        elif a==6:
            send_text_message(reply_token, "好煮義\nhttps://www.google.com/maps/place/%E5%A5%BD%E7%85%AE%E7%BE%A9%E7%BE%A9%E5%A4%A7%E5%88%A9%E9%BA%B5/@22.9949907,120.214856,21z/data=!4m5!3m4!1s0x346e768dc793db25:0x1e0119060e1b497b!8m2!3d22.9949968!4d120.2146983")
        elif a==7:
            send_text_message(reply_token, "惡魔雞排\nhttps://www.google.com/maps/place/%E5%89%B5%E5%A7%8B%E6%83%A1%E9%AD%94%E9%9B%9E%E6%8E%92%E2%80%94%E5%8F%B0%E5%8D%97%E8%82%B2%E6%A8%82%E5%BA%97/@22.9955145,120.2165546,21z/data=!4m5!3m4!1s0x346e770cd6339c13:0xa8204866ab851018!8m2!3d22.9955425!4d120.2165423")
        elif a==8:
            send_text_message(reply_token, "大夯牛排\nhttps://www.google.com/maps/place/%E5%A4%A7%E5%A4%AF%E7%89%9B%E6%8E%92%E9%A4%A8Da-hang+Steak+house/@22.9953082,120.2170482,21z/data=!4m5!3m4!1s0x346e76927bb78707:0xcca908f72b7a20cd!8m2!3d22.9954042!4d120.2171123")
        elif a==9:
            send_text_message(reply_token, "品都炭烤\nhttps://www.google.com/maps/place/%E5%93%81%E9%83%BD%E7%87%92%E7%83%A4+%E6%88%90%E5%A4%A7%E5%BA%97/@22.9955145,120.2165546,21z/data=!4m5!3m4!1s0x346e768d8774afc7:0xbf070f580153bac3!8m2!3d22.9954962!4d120.2165638")
        elif a==10:
            send_text_message(reply_token, "小赤佬\nhttps://www.google.com/maps/place/%E5%B0%8F%E8%B5%A4%E4%BD%AC%E5%B9%B2%E9%8D%8B+%E8%82%B2%E6%A8%82%E5%BA%97/@22.9954169,120.2173373,21z/data=!4m5!3m4!1s0x346e769264b112d7:0xc618979fe2c749d8!8m2!3d22.9954141!4d120.2174013")
        self.go_back()
    def on_enter_state16(self, event):
        reply_token = event.reply_token
        a = random.randint(1,9)
        if a==1:
            send_text_message(reply_token, "豚讚豬排\nhttps://www.google.com/maps/place/%E8%B1%9A%E8%AE%9A%E6%97%A5%E5%BC%8F%E8%B1%AC%E6%8E%92/@22.9917343,120.2176687,19.5z/data=!4m12!1m6!3m5!1s0x346e76938c3a29cd:0xad41338d70f56c8f!2z5Zub5rW36YGK6b6N6Y2L6LK85bCI6LOj5bqXIC0g5Y-w5Y2X6ZW35qau5bqX!8m2!3d22.9937993!4d120.2218518!3m4!1s0x346e7691eb7ea5bd:0x29a2c10c826f02f3!8m2!3d22.9920752!4d120.2179056")
        elif a==2:
            send_text_message(reply_token, "元味屋\nhttps://www.google.com/maps/place/%E5%85%83%E5%91%B3%E5%B1%8B%E5%92%8C%E9%A2%A8%E6%B4%8B%E9%A3%9F/@22.9942822,120.2152823,18.25z/data=!4m12!1m6!3m5!1s0x346e76938c3a29cd:0xad41338d70f56c8f!2z5Zub5rW36YGK6b6N6Y2L6LK85bCI6LOj5bqXIC0g5Y-w5Y2X6ZW35qau5bqX!8m2!3d22.9937993!4d120.2218518!3m4!1s0x346e768db909a2c9:0x258b2672fc2a431e!8m2!3d22.995282!4d120.2146259")
        elif a==3:
            send_text_message(reply_token, "Mr.拉麵\nhttps://www.google.com/maps/place/Mr.%E6%8B%89%E9%BA%B5(%E5%8F%B0%E5%8D%97%E5%BA%97)/@22.9921526,120.2175339,19z/data=!4m5!3m4!1s0x346e7691c037aa79:0xb30c14ea40fa2239!8m2!3d22.9916221!4d120.2178533")
        elif a==4:
            send_text_message(reply_token, "老夫子牛肉麵\nhttps://www.google.com/maps/place/%E8%82%B2%E6%A8%82%E8%A1%97%E8%80%81%E5%A4%AB%E5%AD%90%E7%89%9B%E8%82%89%E9%BA%B5/@22.9939093,120.2147871,19z/data=!4m5!3m4!1s0x346e768dc705d7b9:0x36e2d592127c9cb9!8m2!3d22.9945536!4d120.2145555")
        elif a==5:
            send_text_message(reply_token, "江南美食\nhttps://www.google.com/maps/place/%E6%B1%9F%E5%8D%97%E7%BE%8E%E9%A3%9F+%E9%BB%83%E7%89%9B%E8%82%89%E9%BA%B5(%E5%8F%B0%E5%8D%97%E8%82%B2%E6%A8%82%E5%BA%97)/@22.9947943,120.2151654,19z/data=!4m5!3m4!1s0x0:0x42e6eb4e5997a6c6!8m2!3d22.9949457!4d120.2148123")
        elif a==6:
            send_text_message(reply_token, "麥當勞\nhttps://www.google.com/maps/place/%E9%BA%A5%E7%95%B6%E5%8B%9E-%E5%8F%B0%E5%8D%97%E5%A4%A7%E5%AD%B8%E5%BA%97/@22.9957039,120.2206845,19.25z/data=!4m5!3m4!1s0x346e76936e9b3923:0x8d9e313cba2f84e6!8m2!3d22.9959529!4d120.221369")
        elif a==7:
            send_text_message(reply_token, "肯德基\nhttps://www.google.com/maps/place/%E8%82%AF%E5%BE%B7%E5%9F%BAKFC-%E5%8F%B0%E5%8D%97%E6%88%90%E5%A4%A7%E9%A4%90%E5%BB%B3/@22.9957039,120.2206845,19.25z/data=!4m5!3m4!1s0x346e7693132530db:0xe63489d34fe26cf2!8m2!3d22.9959455!4d120.2209277")
        elif a==8:
            send_text_message(reply_token, "21風味館\nhttps://www.google.com/maps/place/21%E9%A2%A8%E5%91%B3%E9%A4%A8+%E5%8F%B0%E5%8D%97%E6%88%90%E5%A4%A7%E9%96%80%E5%B8%82/@22.9957468,120.2189054,19.25z/data=!4m5!3m4!1s0x0:0xf6abbaf32358f41a!8m2!3d22.9957758!4d120.2182787")
        elif a==9:
            send_text_message(reply_token, "哞王\nhttps://www.google.com/maps/place/%E5%93%9E%E7%8E%8B%E5%8E%9F%E5%91%B3%E7%82%AD%E7%83%A4%E7%89%9B%E6%8E%92/@22.995539,120.2151452,19.25z/data=!4m5!3m4!1s0x346e768d9a7f30c7:0x25ab2e268ce12e33!8m2!3d22.9954906!4d120.2157303")
        self.go_back()
    def on_enter_show_fsm(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
#        send_text_message(reply_token, "Trigger state3")
        send_image(reply_token, 'https://i.imgur.com/yRq0e1U.png')
        self.go_back()
		
