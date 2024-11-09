from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import os

df = pd.read_csv('/home/rohitb/projects/CovidVsIndia/assets/_covid_19_india.csv')
df1 = df.applymap(lambda s: s.lower() if type(s) == str else s)
list_states=[]#list of states chosen
state1,state2,state_list='','',[]
def open(sel_state):
    global state, var1, var2, var3, var4,list_states,state1,state2,state_list
    state = sel_state
    if len(list_states)<2:

        if state not in list_states:
            list_states.append(state)
            state = state.lower()
            state_list.append(state)

    else:
        pass

def done():
    global state, dict_of_graph, list_states, var1, var2, var3, var4,state1,state2,state_list



    def projectH1():
        global state, dict_of_graph,list_states, var1, var2, var3, var4 ,state1,state2,state_list # ,var1,var2,var3,var4

        # MAKING DATAFRAME FOR STATE V/S ALL
        df = pd.read_csv(
            '/home/rohitb/projects/CovidVsIndia/assets/_covid_19_india.csv')  # D:\\class 12 himish\\_covid_19_india.csv
        df1 = df.applymap(lambda s: s.lower() if type(s) == str else s)

        # MAKING DATAFRAME FOR STATE V/S CONFIRMED
        dfconfirmed = pd.read_csv('/home/rohitb/projects/CovidVsIndia/assets/_covid_19_india_confirmed.csv')
        dfconfirmed = dfconfirmed.applymap(lambda s: s.lower() if type(s) == str else s)

        # MAKING DATAFRAME FOR STATE V/S DEATHS
        dfdeaths = pd.read_csv('/home/rohitb/projects/CovidVsIndia/assets/_covid_19_india_deaths.csv')
        dfdeaths = dfdeaths.applymap(lambda s: s.lower() if type(s) == str else s)

        # MAKING DATAFRAME FOR STATE V/S CURED
        dfcured = pd.read_csv('/home/rohitb/projects/CovidVsIndia/assets/_covid_19_india_cured.csv')
        dfcured = dfcured.applymap(lambda s: s.lower() if type(s) == str else s)

        # GIVING THE USER A CHOICE FOR THE TYPE OF GRAPH
        # print ("For \"State v/s confirmed\" type 1","\nFor \"State v/s death\" type 2","\nFor \"State v/s cured\" type 3","\nFor \"State v/s all\" type 4")
        # typeofgraph = int(input("Enter the required number: "))

        # MAKING GRAPH OF STATE V/S CONFIRMED

        if var1.get():
            if len(list_states)==1:
                state = state.strip().lower()

                if state in str(dfconfirmed['State/UnionTerritory'].unique()):
                    # print ('graph for state of ',state.upper(),' ; ')
                    k = dfconfirmed['State/UnionTerritory'] == state
                    kgraph = dfconfirmed[k]
                    kgraph.plot()
                    plt.xlabel('No of Days Passed')
                    plt.ylabel('No of Confirmed Cases')
                    plt.title("Graph of State v/s Confirmed")
                    plt.grid(True)

                    # print (kgraph)
                else:
                    print('Invalid Input')
            else:

                # MAKING CONFIRMED COMPARISION

                if state_list[0] in str(df1['State/UnionTerritory'].unique()) and state_list[1] in str(
                        df1['State/UnionTerritory'].unique()):

                    print('comparision graph for state of ', state1.upper(), ' and ', state2.upper(), ' ; ')
                    k1 = dfconfirmed['State/UnionTerritory'] == state1
                    k2 = dfconfirmed['State/UnionTerritory'] == state2

                    k1graph = dfconfirmed[k1]
                    k2graph = dfconfirmed[k2]

                    fig = plt.figure()

                    for frame in [k1graph, k2graph]:
                        a = []
                        for i in range(1, frame.shape[0] + 1):
                            a.append(i)

                        plt.plot(a, frame['Confirmed'], label=frame.iloc[2, 1])
                        leg = plt.legend()

                        plt.xlabel('No of Days Passed')
                        plt.ylabel('No of Confirmed Cases')
                        plt.title("Graph of State v/s Confirmed")
                        plt.grid(True)

                else:
                    print('Invalid Input')



        # MAKING GRAPH OF STATE V/S DEATHS
        if var2.get():
            if len(list_states) == 1:
                state = state.strip().lower()

                if state in str(df1['State/UnionTerritory'].unique()):
                    # print ('graph for state of ',state.upper(),' ; ')
                    k = dfdeaths['State/UnionTerritory'] == state
                    kgraph = dfdeaths[k]
                    kgraph.plot()
                    plt.xlabel('No of Days Passed')
                    plt.ylabel('No of Confirmed Cases')
                    plt.title("Graph of State v/s Confirmed")
                    plt.grid(True)

                    # print (kgraph)
                else:
                    pass
                    # print('Invalid Input')
            else:
                if state_list[0] in str(df1['State/UnionTerritory'].unique()) and state_list[1] in str(
                        df1['State/UnionTerritory'].unique()):

                    print('comparision graph for state of ', state1.upper(), ' and ', state2.upper(), ' ; ')

                    k1 = dfdeaths['State/UnionTerritory'] == state1
                    k2 = dfdeaths['State/UnionTerritory'] == state2

                    k1graph = dfdeaths[k1]
                    k2graph = dfdeaths[k2]

                    fig = plt.figure()

                    for frame in [k1graph, k2graph]:
                        a = []
                        for i in range(1, frame.shape[0] + 1):
                            a.append(i)

                        plt.plot(a, frame['Deaths'], label=frame.iloc[2, 1])
                        leg = plt.legend()

                        plt.xlabel('No of Days Passed')
                        plt.ylabel('No of Death Cases')
                        plt.title("Graph of State v/s Death")
                        plt.grid(True)

                else:
                    print('Invalid Input')


        # MAKING GRAPH OF STATE V/S CURED
        if var3.get():
            if len(list_states) == 1:
                state = state.strip().lower()

                if state in str(df1['State/UnionTerritory'].unique()):
                    # print ('graph for state of ',state.upper(),' ; ')
                    k = dfcured['State/UnionTerritory'] == state
                    kgraph = dfcured[k]
                    kgraph.plot()
                    plt.xlabel('No of Days Passed')
                    plt.ylabel('No of Confirmed Cases')
                    plt.title("Graph of State v/s Confirmed")
                    plt.grid(True)


                else:
                    pass
                    # print('Invalid Input')

            else:
                if state_list[0] in str(df1['State/UnionTerritory'].unique()) and state_list[1] in str(
                        df1['State/UnionTerritory'].unique()):

                    print('comparision graph for state of ', state1.upper(), ' and ', state2.upper(), ' ; ')

                    k1 = dfcured['State/UnionTerritory'] == state1
                    k2 = dfcured['State/UnionTerritory'] == state2

                    k1graph = dfcured[k1]
                    k2graph = dfcured[k2]

                    fig = plt.figure()

                    for frame in [k1graph, k2graph]:
                        a = []
                        for i in range(1, frame.shape[0] + 1):
                            a.append(i)

                        plt.plot(a, frame['Cured'], label=frame.iloc[2, 1])
                        leg = plt.legend()

                        plt.xlabel('No of Days Passed')
                        plt.ylabel('No of Cured Cases')
                        plt.title("Graph of State v/s cured")
                        plt.grid(True)


                else:
                    print('Invalid Input')




    # MAKING GRAPH OF STATE V/S ALL
        if var4.get():

            state = state.strip().lower()

            if state in str(df1['State/UnionTerritory'].unique()):
                # print ('graph for state of ',state.upper(),' ; ')
                k = df1['State/UnionTerritory'] == state
                kgraph = df1[k]
                kgraph.plot()
                plt.xlabel('No of Days Passed')
                plt.ylabel('No of Confirmed Cases')
                plt.title("Graph of State v/s Confirmed")
                plt.grid(True)

                # print (kgraph)
            else:
                pass
                # print('Invalid Input')
        list_states.clear()
        state_list.clear()
        plt.show()

    def projectH2():
        global state, dict_of_graph, list_states, var1, var2, var3, var4, state1, state2, state_list  # ,var1,var2,var3,var4

        # MAKING DATAFRAME FOR STATE V/S ALL
        df = pd.read_csv(
            '/home/rohitb/projects/CovidVsIndia/assets/_covid_19_india.csv')  # D:\\class 12 himish\\_covid_19_india.csv
        df1 = df.applymap(lambda s: s.lower() if type(s) == str else s)

        # MAKING DATAFRAME FOR STATE V/S CONFIRMED
        dfconfirmed = pd.read_csv('/home/rohitb/projects/CovidVsIndia/assets/_covid_19_india_confirmed.csv')
        dfconfirmed = dfconfirmed.applymap(lambda s: s.lower() if type(s) == str else s)

        # MAKING DATAFRAME FOR STATE V/S DEATHS
        dfdeaths = pd.read_csv('/home/rohitb/projects/CovidVsIndia/assets/_covid_19_india_deaths.csv')
        dfdeaths = dfdeaths.applymap(lambda s: s.lower() if type(s) == str else s)

        # MAKING DATAFRAME FOR STATE V/S CURED
        dfcured = pd.read_csv('/home/rohitb/projects/CovidVsIndia/assets/_covid_19_india_cured.csv')
        dfcured = dfcured.applymap(lambda s: s.lower() if type(s) == str else s)

        # GIVING THE USER A CHOICE FOR THE TYPE OF GRAPH
        # print ("For \"State v/s confirmed\" type 1","\nFor \"State v/s death\" type 2","\nFor \"State v/s cured\" type 3","\nFor \"State v/s all\" type 4")
        # typeofgraph = int(input("Enter the required number: "))

        # MAKING GRAPH OF STATE V/S CONFIRMED
        # MAKING CONFIRMED COMPARISION
        state1 = state_list[0]
        state2 = state_list[1]
        st_list = [state1, state2]
        if state_list[0] in str(df1['State/UnionTerritory'].unique()) and state_list[1] in str(
                df1['State/UnionTerritory'].unique()):

            print('comparision graph for state of ', state1.upper(), ' and ', state2.upper(), ' ; ')
            k1 = dfconfirmed['State/UnionTerritory'] == state1
            k2 = dfconfirmed['State/UnionTerritory'] == state2
            # print(k2)

            k1graph = dfconfirmed[k1]
            k2graph = dfconfirmed[k2]

            fig = plt.figure()
            q = 0

            for frame in [k1graph, k2graph]:
                a = []
                for i in range(1, frame.shape[0] + 1):
                    a.append(i)

                plt.plot(a, frame['Confirmed'], label=st_list[q])
                leg = plt.legend()

                plt.xlabel('No of Days Passed')
                plt.ylabel('No of Confirmed Cases')
                plt.title("Graph of State v/s Confirmed")
                plt.grid(True)
                # print(k1graph)
                q += 1
        else:
            print('Invalid Input')

        # MAKING DEATH COMPARISION

        if state_list[0] in str(df1['State/UnionTerritory'].unique()) and state_list[1] in str(
                df1['State/UnionTerritory'].unique()):

            print('comparision graph for state of ', state1.upper(), ' and ', state2.upper(), ' ; ')

            k1 = dfdeaths['State/UnionTerritory'] == state1
            k2 = dfdeaths['State/UnionTerritory'] == state2
            # print(k2)

            k1graph = dfdeaths[k1]
            k2graph = dfdeaths[k2]

            fig = plt.figure()
            q = 0

            for frame in [k1graph, k2graph]:
                a = []
                for i in range(1, frame.shape[0] + 1):
                    a.append(i)
                # print(a)
                plt.plot(a, frame['Deaths'], label=st_list[q])
                leg = plt.legend()

                plt.xlabel('No of Days Passed')
                plt.ylabel('No of Death Cases')
                plt.title("Graph of State v/s Death")
                plt.grid(True)
                q += 1

        else:
            print('Invalid Input')

        # MAKING CURED COMPARISION

        if state_list[0] in str(df1['State/UnionTerritory'].unique()) and state_list[1] in str(
                df1['State/UnionTerritory'].unique()):

            print('comparision graph for state of ', state1.upper(), ' and ', state2.upper(), ' ; ')

            k1 = dfcured['State/UnionTerritory'] == state1
            k2 = dfcured['State/UnionTerritory'] == state2
            # print(k2)
            k1graph = dfcured[k1]
            k2graph = dfcured[k2]

            fig = plt.figure()
            q = 0

            for frame in [k1graph, k2graph]:
                a = []
                for i in range(1, frame.shape[0] + 1):
                    a.append(i)
                plt.plot(a, frame['Cured'], label=st_list[q])
                leg = plt.legend()

                plt.xlabel('No of Days Passed')
                plt.ylabel('No of Cured Cases')
                plt.title("Graph of State v/s cured")
                plt.grid(True)
                q += 1
        else:
            print('Invalid Input')
        list_states.clear()
        state_list.clear()
        plt.show()

    if len(list_states)==1:
        gui3 = Toplevel()
        gui3.geometry('300x300')
        gui3.title(state)
        var1 = IntVar()

        c1 = Checkbutton(gui3, text='GRAPH OF STATE V/S CONFIRMED', variable=var1, onvalue=1, offvalue=0)

        c1.pack()  # .place(relx=50,rely=10)
        var2 = IntVar()
        c2 = Checkbutton(gui3, text='GRAPH OF STATE V/S DEATHS', variable=var2, onvalue=1,
                         offvalue=0)  # .place(relx=50,rely=50)
        c2.pack()
        var3 = IntVar()
        c3 = Checkbutton(gui3, text='GRAPH OF STATE V/S CURED', variable=var3, onvalue=1,
                         offvalue=0)  # .place(relx=50,rely=90)
        c3.pack()
        if len(list_states)!=2:
            var4 = IntVar()
            c4 = Checkbutton(gui3, text='GRAPH OF STATE V/S ALL', variable=var4, onvalue=1,
                             offvalue=0)  # .place(relx=50,rely=130)
            c4.pack()

        bt = Button(gui3, text='GO!', font=('Ariel', 30), bg='red', fg='white',
                    command=projectH1).pack()  # .place(relx=50,rely=170)
        gui3.mainloop()
    else:
        projectH2()





def start():
    global state
    gui = Toplevel()
    gui.title('STATE')
    canv = Canvas(gui, width=495, height=465)
    canv.pack()
    img = ImageTk.PhotoImage(file='/home/rohitb/projects/CovidVsIndia/assets/india.png')
    canv.create_image(247, 232, image=img)
    bt_jk = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red',
                   command=lambda *args: open('jammu and kashmir'))
    bt_jk_window = canv.create_window(180, 60, window=bt_jk)
    bt_hp = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red',
                   command=lambda *args: open('Himachal Pradesh'))
    bt_hp_window = canv.create_window(200, 90, window=bt_hp)
    bt_p = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red', command=lambda *args: open('Punjab'))
    bt_p_window = canv.create_window(180, 110, window=bt_p)
    bt_u = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red',
                  command=lambda *args: open('Uttarakhand'))
    bt_u_window = canv.create_window(230, 120, window=bt_u)
    bt_h = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red', command=lambda *args: open('Haryana'))
    bt_h_window = canv.create_window(190, 140, window=bt_h)
    bt_up = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red',
                   command=lambda *args: open('Uttar Pradesh'))
    bt_up_window = canv.create_window(250, 170, window=bt_up)
    bt_r = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red', command=lambda *args: open('Rajasthan'))
    bt_r_window = canv.create_window(170, 170, window=bt_r)
    bt_g = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red', command=lambda *args: open('Gujarat'))
    bt_g_window = canv.create_window(130, 220, window=bt_g)
    bt_mp = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red',
                   command=lambda *args: open('Madhya Pradesh'))
    bt_mp_window = canv.create_window(200, 220, window=bt_mp)
    bt_b = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red', command=lambda *args: open('Bihar'))
    bt_b_window = canv.create_window(310, 190, window=bt_b)
    bt_j = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red', command=lambda *args: open('Jharkhand'))
    bt_j_window = canv.create_window(300, 210, window=bt_j)
    bt_wb = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red',
                   command=lambda *args: open('West Bengal'))
    bt_wb_window = canv.create_window(330, 220, window=bt_wb)
    bt_o = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red', command=lambda *args: open('Odisha'))
    bt_o_window = canv.create_window(300, 250, window=bt_o)
    bt_c = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red',
                  command=lambda *args: open('Chhattisgarh'))
    bt_c_window = canv.create_window(260, 250, window=bt_c)
    bt_m = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red',
                  command=lambda *args: open('Maharashtra'))
    bt_m_window = canv.create_window(190, 270, window=bt_m)
    bt_k = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red', command=lambda *args: open('Karnataka'))
    bt_k_window = canv.create_window(180, 340, window=bt_k)
    bt_go = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red', command=lambda *args: open('goa'))
    bt_go_window = canv.create_window(150, 320, window=bt_go)
    bt_t = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red', command=lambda *args: open('Telangana'))
    bt_t_window = canv.create_window(220, 300, window=bt_t)
    bt_ap = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red',
                   command=lambda *args: open('Andhra Pradesh'))
    bt_ap_window = canv.create_window(220, 330, window=bt_ap)
    bt_tn = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red',
                   command=lambda *args: open('Tamil Nadu'))
    bt_tn_window = canv.create_window(220, 370, window=bt_tn)
    bt_ke = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red', command=lambda *args: open('Kerala'))
    bt_ke_window = canv.create_window(190, 390, window=bt_ke)
    bt_s = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red', command=lambda *args: open('Sikkim'))
    bt_s_window = canv.create_window(350, 140, window=bt_s)
    bt_arp = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red',
                    command=lambda *args: open('Arunachal Pradesh'))
    bt_arp_window = canv.create_window(400, 160, window=bt_arp)
    bt_a = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red', command=lambda *args: open('Assam'))
    bt_a_window = canv.create_window(400, 175, window=bt_a)
    bt_me = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red',
                   command=lambda *args: open('Meghalaya'))
    bt_me_window = canv.create_window(380, 185, window=bt_me)
    bt_ng = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red', command=lambda *args: open('Nagaland'))
    bt_ng_window = canv.create_window(420, 175, window=bt_ng)
    bt_mn = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red', command=lambda *args: open('Manipur'))
    bt_mn_window = canv.create_window(420, 200, window=bt_mn)
    bt_mz = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red', command=lambda *args: open('Mizoram'))
    bt_mz_window = canv.create_window(410, 220, window=bt_mz)
    bt_tr = Button(gui, text='', font=('Ariel', 5), width=1, height=1, bg='red', command=lambda *args: open('Tripura'))
    bt_tr_window = canv.create_window(380, 220, window=bt_tr)
    bt_ut_ad = Button(gui, text='Andaman and Nicobar Islands', font=('Ariel', 10), bg='yellow', width=23,
                      command=lambda *args: open('Andaman and Nicobar Islands'))
    bt_ut_ad_window = canv.create_window(400, 298, window=bt_ut_ad)
    bt_ut_c = Button(gui, text='Chandigarh', font=('Ariel', 10), bg='yellow', width=23,
                     command=lambda *args: open('Chandigarh'))
    bt_ut_c_window = canv.create_window(400, 320, window=bt_ut_c)
    bt_ut_dn = Button(gui, text='Dadra and Nagar Haveli', font=('Ariel', 10), bg='yellow', width=23,
                      command=lambda *args: open('Dadra and Nagar Haveli'))
    bt_ut_dn_window = canv.create_window(400, 342, window=bt_ut_dn)
    bt_ut_dd = Button(gui, text='Daman & Diu', font=('Ariel', 10), bg='yellow', width=23,
                      command=lambda *args: open('Daman & Diu'))
    bt_ut_dd_window = canv.create_window(400, 364, window=bt_ut_dd)
    bt_ut_d = Button(gui, text='Delhi', font=('Ariel', 10), bg='yellow', width=23, command=lambda *args: open('Delhi'))
    bt_ut_d_window = canv.create_window(400, 386, window=bt_ut_d)
    bt_ut_l = Button(gui, text='Ladakh', font=('Ariel', 10), bg='yellow', width=23,
                     command=lambda *args: open('Ladakh'))
    bt_ut_l_window = canv.create_window(400, 408, window=bt_ut_l)
    bt_ut_la = Button(gui, text='Lakshadweep', font=('Ariel', 10), bg='yellow', width=23,
                      command=lambda *args: open('Lakshadweep'))
    bt_ut_la_window = canv.create_window(400, 430, window=bt_ut_la)
    bt_ut_p = Button(gui, text='Puducherry', font=('Ariel', 10), bg='yellow', width=23,
                     command=lambda *args: open('Puducherry'))
    bt_ut_p_window = canv.create_window(400, 452, window=bt_ut_p)
    label = Label(canv, text='SELECT THE STATE', font=('Ariel', 10), bg='black', fg='white')
    label_window = canv.create_window(80, 20, window=label)
    bt_done = Button(gui, text='DONE', font=('Ariel', 10), bg='black', fg='white',width=10,command=done)
    bt_done_window=canv.create_window(80, 450, window=bt_done)
    label = Label(canv, text='PROGRAM ACCEPTS', font=('Ariel', 10), bg='black', fg='white')
    label_window = canv.create_window(400, 20, window=label)
    label = Label(canv, text=' ONLY TWO STATES AT A TIME!', font=('Ariel', 10), bg='black', fg='white')
    label_window = canv.create_window(400, 50, window=label)
    gui.mainloop()


window = Tk()
window.configure(bg='black')
window.title('COVID Vs INDIA')
window.geometry('550x550')
for i in range(11):
    for j in range(14):
        label = Label(window, text='  ', fg='black', bg='black').grid(row=i, column=j)
img = ImageTk.PhotoImage(Image.open('/home/rohitb/projects/CovidVsIndia/assets/sars-cov-19_up.jpg'))
panel = Label(window, image=img, bg='black')
panel.grid(row=8, column=15)
label1 = Label(window, text='COVID Vs INDIA', font=('Ariel Bold', 20), fg='white', bg='black').grid(row=12, column=15)
start_bt = Button(window, text='START', font=('Ariel Bold', 15), bg='red', fg='white', command=start).grid(row=13,
                                                                                                           column=15)

window.mainloop()
