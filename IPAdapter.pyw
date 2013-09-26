# -*- coding: utf-8 -*-
'''
Created on 2012-10-30

@author: zslong
'''
import sys
from os import path
import wmi
import time
import threading
import pythoncom
import time

import wx
from wx.lib.masked.ipaddrctrl import IpAddrCtrl
import  wx.lib.buttons  as  buttons
import  wx.lib.rcsizer  as rcs
from wx.lib.embeddedimage import PyEmbeddedImage

Devil = PyEmbeddedImage(
    "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"
    "kwAAAABJRU5ErkJggg==")

wmiService = wmi.WMI()
colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled = True)


class Log(wx.TextCtrl):
    def __init__(self, parent, **kws):
        super(Log, self).__init__(parent, id=-1, style=wx.TE_READONLY|wx.TE_AUTO_SCROLL|wx.TE_MULTILINE, **kws)
        pass
    
    def Write(self, content):
        t = time.strftime('%Y-%m-%d %H:%M:%S')
        
        content = t + '-> ' + content + '\n'
        self.AppendText(content)
        pass
    
class IPAdapterFrame(wx.Frame):
    def __init__(self, parent):
        global Devil
        devil = Devil.GetIcon()
        super(IPAdapterFrame, self).__init__(parent, id = -1, title = u'IP设置', size=(800, 400),
                                             pos = wx.DefaultPosition)
        self.SetIcon(devil)
        self.netState = False #网络连接状态, True:connected, False:disconnected
        
        global colNicConfigs
        
        self.netCfg = colNicConfigs
        try:
            d = eval(file('./ipcfg.txt', 'r').read())
            if isinstance(d, dict):
                self.ncDict = d #key:netcard, value:ipDict
                #self.ipDict = d
            else:
                self.ncDict = {}
        except:
            self.ncDict = {}      
        
        self.panel = panel = wx.Panel(self, -1)
        
        self._InitNetInform()
        if self.netCards != []:
            self.ncCombo = wx.ComboBox(panel, -1, choices=self.netCards, value=self.netCards[0], style=wx.CB_READONLY)
        else:
            self.ncCombo = wx.ComboBox(panel, -1, choices=self.netCards, style=wx.CB_READONLY)
        ipStTxt = wx.StaticText(panel, -1, label=u'IP地址: ')
        snStTxt = wx.StaticText(panel, -1, label=u'子网掩码: ')
        self.ipEdit = IpAddrCtrl(panel)        
        self.snEdit = IpAddrCtrl(panel)
        self.cfgBtn = buttons.GenButton(panel, -1, u'设置')
        self.delBtn = buttons.GenButton(panel, -1, u'删除')
        self.autoBtn = buttons.GenButton(panel, -1, u'自动获取')
        self.saveBtn = buttons.GenButton(panel, -1, u'保存')
        self.log = Log(panel)
        self.ipList = wx.ListCtrl(panel, -1, style = wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)
        
        sysConfig = self.ipDict.get('system IP')
        if isinstance(sysConfig, tuple):
            self.ipEdit.SetValue(sysConfig[0])
            self.snEdit.SetValue(sysConfig[1])
        self._InitListContent()
        
        
        
        #--layouts
        szr = wx.BoxSizer(wx.HORIZONTAL)
        grdszr = wx.FlexGridSizer(3, 2, 5, 5)
        grdszr.AddMany([(ipStTxt, 0, wx.EXPAND), (self.ipEdit, 0, wx.EXPAND),
                        (snStTxt, 0, wx.EXPAND), (self.snEdit, 0, wx.EXPAND),
                        (self.autoBtn, 0, wx.EXPAND),(self.cfgBtn, 0, wx.EXPAND)])
        #grdszr.AddGrowableRow(0)
        grdszr.AddGrowableCol(1)
        hszr1 = wx.BoxSizer(wx.HORIZONTAL)  
        hszr2 = wx.BoxSizer(wx.HORIZONTAL)      
        vszr1 = wx.BoxSizer(wx.VERTICAL)
        vszr2 = wx.BoxSizer(wx.VERTICAL)
        vszr3 = wx.BoxSizer(wx.VERTICAL)
        hszr1.AddMany([(5,5), (self.saveBtn, 0, wx.EXPAND), (5,5), (self.delBtn, 0, wx.EXPAND), (5,5)])
        vszr1.AddMany([(self.ipList, 1, wx.EXPAND), (5,5), (hszr1, 0, wx.ALIGN_RIGHT)])
        vszr2.AddMany([(5,5), (grdszr, 1, wx.EXPAND), (5,5), (vszr1, 3, wx.EXPAND), (5,5)])
        #vszr2.AddMany([(grdszr, 1, wx.EXPAND), (5,5), (self.cfgBtn, 0, wx.ALIGN_RIGHT)])
        hszr2.AddMany([(wx.StaticText(panel,-1,label=u'请选择网卡:'), 0, wx.ALIGN_CENTER),(5,5),(self.ncCombo, 1, wx.EXPAND)])
        vszr3.AddMany([(5,5), (hszr2, 0, wx.EXPAND), (5,5), (self.log,1, wx.EXPAND), (5,5)])
        szr.AddMany([ (5,5), (vszr2, 1, wx.EXPAND), (5,5), (vszr3, 4, wx.EXPAND), (5,5)])
        panel.SetSizerAndFit(szr)
        pass
    
        # -- bind events
        self.Bind(wx.EVT_BUTTON, self.OnConfig, self.cfgBtn)
        self.Bind(wx.EVT_BUTTON, self.OnAutoAquire, self.autoBtn)
        self.Bind(wx.EVT_BUTTON, self.OnSave, self.saveBtn)
        self.Bind(wx.EVT_BUTTON, self.OnDel, self.delBtn)
        self.ipList.Bind(wx.EVT_LEFT_DCLICK, self.OnDoubleClick)
        self.ncCombo.Bind(wx.EVT_COMBOBOX, self.OnNetCardChanged)
        
        #监视网络连接线程
        thrd = threading.Thread(target=self.NetListener)
        thrd.setDaemon(True)
        thrd.start()
        
    def _InitNetInform(self):
        sysIp = None
        sysSubnet = None
        self.netCards = []
        self.netCard = ''
        for interface in self.netCfg:   
            #if 'Wireless' in interface.Description: continue
            netCard = interface.Description
            if self.ncDict != {}:
                ipDict = self.ncDict.get(netCard, None)
                if ipDict is None:
                    ipDict = {}
            else:
                ipDict = {}                
            self.netCards.append(netCard)
            sysIp = interface.IPAddress[0]
            sysSubnet = interface.IPSubnet[0]
            ipDict['system IP'] = (sysIp, sysSubnet)
            ipDict[sysIp] = sysSubnet
            self.ncDict[netCard] = ipDict
        if self.netCards != []:
            self.netCard = self.netCards[0] 
        self.interface = None
        for i in self.netCfg:
            if i.Description == self.netCard:
                self.interface = i
        if self.netCard != '':
            self.netState = True
            self.ipDict = self.ncDict[self.netCard]
        else:
            self.ipDict = {}
            self.log.Write(u'没有检测到网络连接！')
        pass
        
    def _InitListContent(self):
        # first delte all columes and items in list
        self.ipList.DeleteAllColumns()
        self.ipList.DeleteAllItems()
        
        self.ipList.InsertColumn(0, u'IP地址', width=100)
        self.ipList.InsertColumn(1, u'子网掩码', width=100)
        index = 0
        for k in self.ipDict:
            if k == 'system IP':
                continue
            self.ipList.InsertStringItem(index, k)
            self.ipList.SetStringItem(index, 1, self.ipDict[k])
            index += 1
            pass
        pass
        
    def NetListener(self):
        pythoncom.CoInitialize()#线程同步？
        wmiService = wmi.WMI()
        while True:            
            cfg = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled = True)
            self.netCfg = cfg
            if cfg == []:#网络断开
                if self.netState == True:  
                    self._InitNetInform()
                    self.ncCombo.Clear()
                    self.ipEdit.Clear()  
                    self.snEdit.Clear()
                    self._InitListContent()                
                    self.netState = False
                    wx.CallAfter(self.Warn, self.netState)
            elif cfg != []:
                if self.netState == False:
                    self._InitNetInform()
                    self.ncCombo.Set(self.netCards)
                    self.ncCombo.SetValue(self.netCard)
                    sysConfig = self.ipDict.get('system IP')
                    if isinstance(sysConfig, tuple):
                        self.ipEdit.SetValue(sysConfig[0])
                        self.snEdit.SetValue(sysConfig[1])
                    self._InitListContent()
                    self.netState = True
                    wx.CallAfter(self.Warn, self.netState) 
            time.sleep(1)                   
        pass
    
    def Warn(self, netState):
        if netState:
            self.log.Write(u'网络重新连接')
        else:
            self.log.Write(u'网络断开')
        
        
    def OnNetCardChanged(self, evt):
        self.netCard = evt.GetString()
        for i in self.netCfg:
            if i.Description == self.netCard:
                self.interface = i
        self.ipDict = self.ncDict[self.netCard]
        sysConfig = self.ipDict.get('system IP')
        if isinstance(sysConfig, tuple):
            self.ipEdit.SetValue(sysConfig[0])
            self.snEdit.SetValue(sysConfig[1])
        self._InitListContent()
        pass
    

    def OnAutoAquire(self, evt):
        rtv = self.interface.EnableDHCP()
        reboot = 0
        try:
            ip = self.interface.IPAddress[0]
            sn = self.interface.IPSubnet[0]
            if rtv[0] == 0:
                self.log.Write(u'设置自动获取成功')
                self.ipEdit.SetValue(ip)
                self.snEdit.SetValue(sn)
            elif rtv[0] == 1:
                self.log.Write(u'设置自动获取成功')
                self.ipEdit.SetValue(ip)
                self.snEdit.SetValue(sn)
                reboot += 1
            else:
                self.log.Write(u'设置自动获取失败')
            if reboot > 1:
                self.log.Write( u'需要重启计算机')
        except:
            self.log.Write(u'请检查网线是否插好或无线网是否开启！')
            wx.MessageBox(u'请检查网线是否插好或无线网是否开启！')       
        pass
    def OnDoubleClick(self, evt):
        curSel = self.ipList.GetFirstSelected()
        
        ip = self.ipList.GetItemText(curSel)
        sn = self.ipList.GetItemText(curSel, 1)
        self.ipEdit.SetValue(ip)
        self.snEdit.SetValue(sn)
        pass
        
    def OnSave(self, evt):
        try:
            fp = './ipcfg.txt'
            file(fp, 'w').write(str(self.ncDict))
            self.log.Write(u'配置保存至:'+path.abspath(fp))
        except Exception, e:
            self.log.Write(u'配置保存失败'+str(e))
            pass
        pass
    
    def OnDel(self, evt):
        index = self.ipList.GetFirstSelected()
        ip = self.ipList.GetItemText(index)
        self.ipList.DeleteItem(index)
        del self.ipDict[ip]
        pass
    
    def OnConfig(self, evt):
        ip = self.ipEdit.GetAddress()
        sn = self.snEdit.GetAddress()
        try:
            rtv = self.interface.EnableStatic(IPAddress = [ip], SubnetMask = [sn])
            reboot = 0 
            if rtv[0] == 0:
                self.ipDict[ip] = sn
                self.log.Write(u'设置IP成功'+'\n\t\t\t'+u'IP地址:'+ip+'\n\t\t\t'+u'子网掩码:'+sn) 
                self._InitListContent()
            elif rtv[0] == 1:
                self.ipDict[ip] = sn
                self.log.Write(u'设置IP成功'+'\n\t\t\t'+u'IP地址:'+ip+'\n\t\t\t'+u'子网掩码:'+sn) 
                reboot += 1
                self._InitListContent()
            else:
                self.log.Write(u'设置IP失败') 
            
            if reboot > 1:
                self.log.Write( u'需要重启计算机')
        except:
            self.log.Write(u'请检查网线是否插好或无线网是否开启！')
            wx.MessageBox(u'请检查网线是否插好或无线网是否开启！')
            
        pass
class MainApp(wx.App):
    def OnInit(self):
        frm = IPAdapterFrame(None)
        frm.Show()
        return True
if __name__ == '__main__':
    main = MainApp()
    main.MainLoop()
    pass


