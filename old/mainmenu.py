#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.3 on Thu Sep  6 03:05:56 2018
#

import wx
import subprocess

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

class dialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((381, 264))
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.btnHarddiskExtraction = wx.Button(self.panel_1, wx.ID_ANY, "Hard disk extraction")
        self.btnMobileExtraction = wx.Button(self.panel_1, wx.ID_ANY, "Mobile extraction")
        self.btnNetworkAnalysis = wx.Button(self.panel_1, wx.ID_ANY, "Network analysis")
        self.btnExit = wx.Button(self.panel_1, wx.ID_ANY, "Close")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.onBtnHarddiskExtraction, self.btnHarddiskExtraction)
        self.Bind(wx.EVT_BUTTON, self.onBtnMobileExtraction, self.btnMobileExtraction)
        self.Bind(wx.EVT_BUTTON, self.onBtnNetworkAnalysis, self.btnNetworkAnalysis)
        self.Bind(wx.EVT_BUTTON, self.onExit, self.btnExit)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: mainMenu.__set_properties
        self.SetTitle("Forensic Pi")
        self.btnHarddiskExtraction.SetMinSize((138, 21))
        self.btnMobileExtraction.SetMinSize((138, 21))
        self.btnNetworkAnalysis.SetMinSize((138, 21))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: mainMenu.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "Forensic Pi")
        label_1.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        sizer_2.Add(label_1, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        sizer_2.Add(self.btnHarddiskExtraction, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer_2.Add(self.btnMobileExtraction, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer_2.Add(self.btnNetworkAnalysis, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer_3.Add((300, 20), 0, 0, 0)
        sizer_3.Add(self.btnExit, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def onBtnHarddiskExtraction(self, event):  # wxGlade: mainMenu.<event_handler>
        self.Close()
        self.Destroy()

    def onBtnMobileExtraction(self, event):  # wxGlade: mainMenu.<event_handler>
        print("Event handler 'onBtnMobileExtraction' not implemented!")
        event.Skip()

    def onBtnNetworkAnalysis(self, event):  # wxGlade: mainMenu.<event_handler>
        subprocess.check_call(["python", "/home/pi/Desktop/Codes/NAdialog.py"])


    def onExit(self, event):  # wxGlade: mainMenu.<event_handler>
        self.Close()
        self.Destroy()
        

# end of class mainMenu

# class menu(wx.App):
#     def OnInit(self):
#         self.frame = mainMenu(None, wx.ID_ANY, "")
#         self.SetTopWindow(self.frame)
#         self.frame.Show()
#         return True

# # # end of class menu

# if __name__ == "__main__":
#     mainMenu = menu(0)
#     mainMenu.MainLoop()
