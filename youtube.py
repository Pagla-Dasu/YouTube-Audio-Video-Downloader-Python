import shutil
import pyautogui
import time
from moviepy.editor import *
import threading
import multiprocessing
from pafy import *
import humanize
import requests
import urllib
import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *


class Ui_mainWindow(object):
	def setupUi(self, mainWindow):
		mainWindow.setObjectName("mainWindow")
		mainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
		mainWindow.setEnabled(True)
		mainWindow.resize(1920, 1080)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
		mainWindow.setSizePolicy(sizePolicy)
		mainWindow.setMinimumSize(QtCore.QSize(800, 600))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("youtube.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		mainWindow.setWindowIcon(icon)
		mainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
		mainWindow.setIconSize(QtCore.QSize(64, 64))
		mainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks)
		self.centralwidget = QtWidgets.QWidget(mainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
		self.tableWidget.setGeometry(QtCore.QRect(10, 30, 851, 581))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.tableWidget.setFont(font)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setColumnCount(6)
		self.tableWidget.setRowCount(0)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(4, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(5, item)
		self.tableWidget.setShowGrid(False)
		self.preview = QtWidgets.QFrame(self.centralwidget)
		self.preview.setGeometry(QtCore.QRect(870, 0, 1041, 561))
		self.preview.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.preview.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.preview.setObjectName("preview")
		self.graphicsPlayer = QtWidgets.QGraphicsView(self.preview)
		self.graphicsPlayer.setGeometry(QtCore.QRect(0, 0, 1041, 561))
		self.graphicsPlayer.setObjectName("graphicsPlayer")
		self.pushBack = QtWidgets.QPushButton(self.centralwidget)
		self.pushBack.setGeometry(QtCore.QRect(1150, 570, 171, 41))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.pushBack.setFont(font)
		self.pushBack.setText("")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("multimedia-option.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.pushBack.setIcon(icon1)
		self.pushBack.setIconSize(QtCore.QSize(20, 20))
		self.pushBack.setFlat(True)
		self.pushBack.setObjectName("pushBack")
		self.pushplay = QtWidgets.QPushButton(self.centralwidget)
		self.pushplay.setGeometry(QtCore.QRect(1310, 570, 161, 41))
		self.pushplay.setText("")
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap("shapes-and-symbols.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.pushplay.setIcon(icon2)
		self.pushplay.setIconSize(QtCore.QSize(20, 20))
		self.pushplay.setFlat(True)
		self.pushplay.setObjectName("pushplay")
		self.pushnext = QtWidgets.QPushButton(self.centralwidget)
		self.pushnext.setGeometry(QtCore.QRect(1460, 570, 161, 41))
		self.pushnext.setText("")
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap("left-and-right-arrows.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.pushnext.setIcon(icon3)
		self.pushnext.setIconSize(QtCore.QSize(20, 20))
		self.pushnext.setFlat(True)
		self.pushnext.setObjectName("pushnext")
		self.webpage = QtWidgets.QFrame(self.centralwidget)
		self.webpage.setGeometry(QtCore.QRect(10, 650, 1901, 381))
		self.webpage.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.webpage.setFrameShadow(QtWidgets.QFrame.Plain)
		self.webpage.setObjectName("webpage")
		self.graphicsWebpage = QtWidgets.QGraphicsView(self.webpage)
		self.graphicsWebpage.setGeometry(QtCore.QRect(0, 0, 1901, 381))
		self.graphicsWebpage.setObjectName("graphicsWebpage")
		self.DownloadVideo = QtWidgets.QPushButton(self.centralwidget)
		self.DownloadVideo.setGeometry(QtCore.QRect(900, 570, 201, 41))
		self.DownloadVideo.setAutoFillBackground(False)
		self.DownloadVideo.setText("")
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap("web.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.DownloadVideo.setIcon(icon4)
		self.DownloadVideo.setIconSize(QtCore.QSize(64, 32))
		self.DownloadVideo.setCheckable(False)
		self.DownloadVideo.setAutoExclusive(False)
		self.DownloadVideo.setAutoDefault(False)
		self.DownloadVideo.setDefault(False)
		self.DownloadVideo.setFlat(False)
		self.DownloadVideo.setObjectName("DownloadVideo")
		self.DownloadAudio = QtWidgets.QPushButton(self.centralwidget)
		self.DownloadAudio.setGeometry(QtCore.QRect(1680, 570, 201, 41))
		self.DownloadAudio.setText("")
		icon5 = QtGui.QIcon()
		icon5.addPixmap(QtGui.QPixmap("music.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.DownloadAudio.setIcon(icon5)
		self.DownloadAudio.setIconSize(QtCore.QSize(64, 32))
		self.DownloadAudio.setObjectName("DownloadAudio")
		self.frame = QtWidgets.QFrame(self.centralwidget)
		self.frame.setGeometry(QtCore.QRect(10, 620, 1901, 31))
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
		self.frame.setObjectName("frame")
		self.control = QtWidgets.QFrame(self.frame)
		self.control.setGeometry(QtCore.QRect(0, 0, 1901, 31))
		self.control.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.control.setFrameShadow(QtWidgets.QFrame.Raised)
		self.control.setObjectName("control")
		self.webpageback = QtWidgets.QPushButton(self.control)
		self.webpageback.setGeometry(QtCore.QRect(10, 5, 41, 23))
		self.webpageback.setText("")
		icon6 = QtGui.QIcon()
		icon6.addPixmap(QtGui.QPixmap("directional.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.webpageback.setIcon(icon6)
		self.webpageback.setFlat(True)
		self.webpageback.setObjectName("webpageback")
		self.webpagefront = QtWidgets.QPushButton(self.control)
		self.webpagefront.setGeometry(QtCore.QRect(70, 5, 41, 23))
		self.webpagefront.setText("")
		icon7 = QtGui.QIcon()
		icon7.addPixmap(QtGui.QPixmap("forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.webpagefront.setIcon(icon7)
		self.webpagefront.setFlat(True)
		self.webpagefront.setObjectName("webpagefront")
		self.webpagerefresh = QtWidgets.QPushButton(self.control)
		self.webpagerefresh.setGeometry(QtCore.QRect(130, 5, 41, 23))
		self.webpagerefresh.setText("")
		icon8 = QtGui.QIcon()
		icon8.addPixmap(QtGui.QPixmap("rss-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.webpagerefresh.setIcon(icon8)
		self.webpagerefresh.setFlat(True)
		self.webpagerefresh.setObjectName("webpagerefresh")
		self.webpagelabel = QtWidgets.QLabel(self.control)
		self.webpagelabel.setGeometry(QtCore.QRect(610, 0, 731, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.webpagelabel.setFont(font)
		self.webpagelabel.setScaledContents(True)
		self.webpagelabel.setAlignment(QtCore.Qt.AlignCenter)
		self.webpagelabel.setWordWrap(True)
		self.webpagelabel.setObjectName("webpagelabel")
		self.frame_upper = QtWidgets.QFrame(self.centralwidget)
		self.frame_upper.setGeometry(QtCore.QRect(10, 0, 851, 31))
		self.frame_upper.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_upper.setFrameShadow(QtWidgets.QFrame.Plain)
		self.frame_upper.setObjectName("frame_upper")
		self.labelurl = QtWidgets.QLabel(self.frame_upper)
		self.labelurl.setGeometry(QtCore.QRect(6, -5, 71, 41))
		self.labelurl.setText("")
		self.labelurl.setPixmap(QtGui.QPixmap("html.png"))
		self.labelurl.setScaledContents(True)
		self.labelurl.setAlignment(QtCore.Qt.AlignCenter)
		self.labelurl.setWordWrap(False)
		self.labelurl.setObjectName("labelurl")
		self.urltext = QtWidgets.QLineEdit(self.frame_upper)
		self.urltext.setGeometry(QtCore.QRect(80, 3, 701, 25))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.urltext.setFont(font)
		self.urltext.setInputMask("")
		self.urltext.setText("")
		self.urltext.setClearButtonEnabled(True)
		self.urltext.setObjectName("urltext")
		self.searchbutton = QtWidgets.QPushButton(self.frame_upper)
		self.searchbutton.setGeometry(QtCore.QRect(780, 0, 71, 31))
		self.searchbutton.setText("")
		icon9 = QtGui.QIcon()
		icon9.addPixmap(QtGui.QPixmap("analytics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.searchbutton.setIcon(icon9)
		self.searchbutton.setIconSize(QtCore.QSize(25, 25))
		self.searchbutton.setFlat(True)
		self.searchbutton.setObjectName("searchbutton")
		mainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(mainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
		self.menubar.setObjectName("menubar")
		self.menuFile = QtWidgets.QMenu(self.menubar)
		self.menuFile.setObjectName("menuFile")
		self.menuEdit = QtWidgets.QMenu(self.menubar)
		self.menuEdit.setObjectName("menuEdit")
		self.menuHelp = QtWidgets.QMenu(self.menubar)
		self.menuHelp.setObjectName("menuHelp")
		self.menuTools = QtWidgets.QMenu(self.menubar)
		self.menuTools.setObjectName("menuTools")
		mainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(mainWindow)
		self.statusbar.setObjectName("statusbar")
		mainWindow.setStatusBar(self.statusbar)
		self.actionNew = QtWidgets.QAction(mainWindow)
		self.actionNew.setObjectName("actionNew")
		self.actionOpen = QtWidgets.QAction(mainWindow)
		self.actionOpen.setObjectName("actionOpen")
		self.actionSave = QtWidgets.QAction(mainWindow)
		self.actionSave.setObjectName("actionSave")
		self.actionSave_As = QtWidgets.QAction(mainWindow)
		self.actionSave_As.setObjectName("actionSave_As")
		self.actionConsole = QtWidgets.QAction(mainWindow)
		self.actionConsole.setObjectName("actionConsole")
		self.actionExit = QtWidgets.QAction(mainWindow)
		self.actionExit.setObjectName("actionExit")
		self.actionCopy = QtWidgets.QAction(mainWindow)
		self.actionCopy.setObjectName("actionCopy")
		self.actionPaste = QtWidgets.QAction(mainWindow)
		self.actionPaste.setObjectName("actionPaste")
		self.actionCut = QtWidgets.QAction(mainWindow)
		self.actionCut.setObjectName("actionCut")
		self.actionAbout_Youtube_Downloader = QtWidgets.QAction(mainWindow)
		self.actionAbout_Youtube_Downloader.setObjectName("actionAbout_Youtube_Downloader")
		self.actionHow_to_Download = QtWidgets.QAction(mainWindow)
		self.actionHow_to_Download.setObjectName("actionHow_to_Download")
		self.actionHow_to_download_Audio = QtWidgets.QAction(mainWindow)
		self.actionHow_to_download_Audio.setObjectName("actionHow_to_download_Audio")
		self.actionConvert_to_mp3 = QtWidgets.QAction(mainWindow)
		self.actionConvert_to_mp3.setObjectName("actionConvert_to_mp3")
		self.actionSpeed_Test = QtWidgets.QAction(mainWindow)
		self.actionSpeed_Test.setObjectName("actionSpeed_Test")
		self.menuFile.addAction(self.actionNew)
		self.menuFile.addAction(self.actionSave)
		self.menuFile.addSeparator()
		self.menuFile.addAction(self.actionConsole)
		self.menuFile.addAction(self.actionExit)
		self.menuEdit.addAction(self.actionCopy)
		self.menuEdit.addAction(self.actionPaste)
		self.menuEdit.addAction(self.actionCut)
		self.menuHelp.addAction(self.actionHow_to_Download)
		self.menuHelp.addAction(self.actionHow_to_download_Audio)
		self.menuHelp.addAction(self.actionAbout_Youtube_Downloader)
		self.menuTools.addAction(self.actionConvert_to_mp3)
		self.menuTools.addAction(self.actionSpeed_Test)
		self.menubar.addAction(self.menuFile.menuAction())
		self.menubar.addAction(self.menuEdit.menuAction())
		self.menubar.addAction(self.menuTools.menuAction())
		self.menubar.addAction(self.menuHelp.menuAction())

		self.retranslateUi(mainWindow)
		QtCore.QMetaObject.connectSlotsByName(mainWindow)
		mainWindow.setTabOrder(self.tableWidget, self.pushBack)
		mainWindow.setTabOrder(self.pushBack, self.pushnext)
		mainWindow.setTabOrder(self.pushnext, self.DownloadVideo)
		mainWindow.setTabOrder(self.DownloadVideo, self.DownloadAudio)
		mainWindow.setTabOrder(self.DownloadAudio, self.webpageback)
		mainWindow.setTabOrder(self.webpageback, self.webpagefront)
		mainWindow.setTabOrder(self.webpagefront, self.pushplay)
		mainWindow.setTabOrder(self.pushplay, self.webpagerefresh)
		mainWindow.setTabOrder(self.webpagerefresh, self.graphicsWebpage)
		mainWindow.setTabOrder(self.graphicsWebpage, self.graphicsPlayer)
		mainWindow.setTabOrder(self.graphicsPlayer, self.urltext)
		mainWindow.setTabOrder(self.urltext, self.searchbutton)

		self.web = QWebEngineView(self.graphicsWebpage)
		self.web.setGeometry(2, 1, 1896, 370)
		self.web.load(QtCore.QUrl("https://www.youtube.com"))
		self.web.urlChanged.connect(self.lab)
		self.web.page().setAudioMuted(True)
		self.web.show()
		self.webpageback.clicked.connect(lambda: self.web.back())
		self.webpagefront.clicked.connect(lambda: self.web.forward())
		self.webpagerefresh.clicked.connect(lambda: self.web.reload())
		self.web.thread()
		
		# width="1020" height="540"
		self.you = QWebEngineView(self.graphicsPlayer)
		self.you.setGeometry(2, 2, 1036, 556)
		self.you.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
		self.you.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
		self.you.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
		self.you.page().fullScreenRequested.connect(lambda request: request.accept())
		self.baseUrl = "local"
		self.htmlString = """
				   <iframe width="1020" height="540" src="https://www.youtube.com/embed/lPZRmkVLeOE?feature=oembed;&autoplay=1" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
					"""
		self.you.setHtml(self.htmlString, QtCore.QUrl(self.baseUrl))
		self.you.loadFinished.connect(self.now)
		self.you.hide()
		self.you.adjustSize()
		self.you.thread()

		self.DownloadVideo.setEnabled(False)
		self.DownloadAudio.setEnabled(False)

		self.DownloadVideo.clicked.connect(self.download_video)
		self.DownloadAudio.clicked.connect(self.download_audio)
		self.searchbutton.clicked.connect(self.go_to)

		self.rownumber = 0

	def now(self):
		x, y = pyautogui.position()
		pyautogui.doubleClick(1240, 300, interval=0.2)
		pyautogui.moveTo(x, y)
		self.webpageback.click()
		self.web.show()

	def download_video(self):
		self.Dialog = QtWidgets.QDialog(self.centralwidget)
		self.Dialog.setModal(True)
		self.Dialog.setEnabled(True)
		self.Dialog.resize(541, 421)
		self.Dialog.thread()
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("web.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.Dialog.setWindowIcon(icon)
		self.Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
		
		self.label = QtWidgets.QLabel(self.Dialog)
		self.label.setGeometry(QtCore.QRect(20, 20, 61, 21))
		self.label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setOpenExternalLinks(False)
		self.label.setObjectName("label")
		self.youtube_title = QtWidgets.QLabel(self.Dialog)
		self.youtube_title.setGeometry(QtCore.QRect(100, 20, 391, 21))
		self.youtube_title.setObjectName("youtube_title")
		self.label_2 = QtWidgets.QLabel(self.Dialog)
		self.label_2.setGeometry(QtCore.QRect(20, 60, 61, 21))
		self.label_2.setObjectName("label_2")
		self.channel_name = QtWidgets.QLabel(self.Dialog)
		self.channel_name.setGeometry(QtCore.QRect(100, 60, 391, 21))
		self.channel_name.setObjectName("channel_name")
		self.label_4 = QtWidgets.QLabel(self.Dialog)
		self.label_4.setGeometry(QtCore.QRect(20, 100, 61, 21))
		self.label_4.setAlignment(QtCore.Qt.AlignCenter)
		self.label_4.setObjectName("label_4")
		self.view_count = QtWidgets.QLabel(self.Dialog)
		self.view_count.setGeometry(QtCore.QRect(100, 100, 191, 21))
		self.view_count.setObjectName("view_count")
		self.label_6 = QtWidgets.QLabel(self.Dialog)
		self.label_6.setGeometry(QtCore.QRect(20, 140, 61, 21))
		self.label_6.setAlignment(QtCore.Qt.AlignCenter)
		self.label_6.setObjectName("label_6")
		self.likes = QtWidgets.QLabel(self.Dialog)
		self.likes.setGeometry(QtCore.QRect(100, 140, 91, 21))
		self.likes.setObjectName("likes")
		self.label_8 = QtWidgets.QLabel(self.Dialog)
		self.label_8.setGeometry(QtCore.QRect(220, 140, 61, 21))
		self.label_8.setAlignment(QtCore.Qt.AlignCenter)
		self.label_8.setObjectName("label_8")
		self.dislikes = QtWidgets.QLabel(self.Dialog)
		self.dislikes.setGeometry(QtCore.QRect(300, 140, 91, 21))
		self.dislikes.setObjectName("dislikes")
		self.textBrowser = QtWidgets.QTextBrowser(self.Dialog)
		self.textBrowser.setGeometry(QtCore.QRect(50, 190, 371, 31))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.textBrowser.setFont(font)
		self.textBrowser.setFocusPolicy(QtCore.Qt.NoFocus)
		self.textBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
		self.textBrowser.setObjectName("textBrowser")
		self.save = QtWidgets.QPushButton(self.Dialog)
		self.save.setGeometry(QtCore.QRect(440, 190, 41, 31))
		self.save.setFocusPolicy(QtCore.Qt.NoFocus)
		self.save.setText("")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("click.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.save.setIcon(icon1)
		self.save.setIconSize(QtCore.QSize(30, 30))
		self.save.setObjectName("save")
		self.comboBox = QtWidgets.QComboBox(self.Dialog)
		self.comboBox.setGeometry(QtCore.QRect(150, 260, 231, 21))
		self.comboBox.setObjectName("comboBox")
		self.label_7 = QtWidgets.QLabel(self.Dialog)
		self.label_7.setGeometry(QtCore.QRect(30, 250, 111, 41))
		self.label_7.setAlignment(QtCore.Qt.AlignCenter)
		self.label_7.setObjectName("label_7")
		self.progressBar = QtWidgets.QProgressBar(self.Dialog)
		self.progressBar.setGeometry(QtCore.QRect(30, 310, 481, 23))
		self.progressBar.setProperty("value", 0)
		self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
		self.progressBar.setObjectName("progressBar")
		self.pushButton = QtWidgets.QPushButton(self.Dialog)
		self.pushButton.setGeometry(QtCore.QRect(170, 370, 201, 31))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.pushButton.setFont(font)
		self.pushButton.setObjectName("pushButton")

		self.video = pafy.new(self.you.page().requestedUrl().toString())

		self.youtube_title.setText(self.video.title)
		self.youtube_title.adjustSize()

		self.channel_name.setText(self.video.author)
		self.channel_name.adjustSize()

		self.view_count.setText(str(self.video.viewcount))
		self.view_count.adjustSize()

		self.likes.setText(str(self.video.likes))
		self.likes.adjustSize()

		self.dislikes.setText(str(self.video.dislikes))
		self.dislikes.adjustSize()

		self.combo = []
		data = self.get_video_data()
		self.comboBox.addItems(data)
		self.save.clicked.connect(self.save_location)
		self.pushButton.clicked.connect(self.download)

		# self.Dialog.adjustSize()
		self.Dialog.setFixedSize(self.Dialog.size())
		self.Dialog.show()

		self.retranslateUi_Dialog(self.Dialog)
		QtCore.QMetaObject.connectSlotsByName(self.Dialog)

	def retranslateUi_Dialog(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		self.Dialog.setWindowTitle(_translate("self.Dialog", "Download Video"))
		self.label.setText(_translate("self.Dialog", "TITLE :-"))
		# self.youtube_title.setText(_translate("self.Dialog", "YOUTUBE TITLE"))
		self.label_2.setText(_translate("self.Dialog", "CHANNEL :-"))
		# self.channel_name.setText(_translate("self.Dialog", "CHANNEL NAME"))
		self.label_4.setText(_translate("self.Dialog", "VIEWS :-"))
		# self.view_count.setText(_translate("self.Dialog", "VIEWS"))
		self.label_6.setText(_translate("self.Dialog", "LIKES :-"))
		# self.likes.setText(_translate("self.Dialog", "LIKE_NO"))
		self.label_8.setText(_translate("self.Dialog", "DISLIKES:-"))
		# self.dislikes.setText(_translate("self.Dialog", "DISLIKE_NO"))
		self.textBrowser.setPlaceholderText(_translate("self.Dialog", "Click the button to choose a folder."))
		self.label_7.setText(_translate("self.Dialog", "Select Quality :-"))
		self.progressBar.setFormat(_translate("self.Dialog", "%p%"))
		self.pushButton.setText(_translate("self.Dialog", "Download"))

	def get_video_data(self):
		i = 0
		streams = self.video.videostreams
		for stream in streams:
			i += 1
			size = humanize.naturalsize(stream.get_filesize())
			# data = "{} {} {} {} ".format(stream.mediatype, stream.extension, stream.quality, size)
			data = str(i) + ". " + str(stream.extension) + " " + str(stream.quality) + " " + str(size)
			self.combo.append(data)
		return self.combo

	def get_audio_data(self):
		i = 0
		streams = self.audio.audiostreams
		for stream in streams:
			i += 1
			size = humanize.naturalsize(stream.get_filesize())
			# data = "{} {} {} {} ".format(stream.mediatype, stream.extension, stream.quality, size)
			data = str(i) + ". " + str(stream.extension) + " " + str(stream.quality) + " " + str(size)
			self.combo.append(data)
		return self.combo

	def save_location(self):
		store = QtWidgets.QFileDialog.getExistingDirectory()
		self.textBrowser.setText(store)

	def download_audio(self):
		self.Dialog = QtWidgets.QDialog(self.centralwidget)
		self.Dialog.setModal(True)
		self.Dialog.setEnabled(True)
		self.Dialog.resize(541, 421)
		self.Dialog.thread()
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("music.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.Dialog.setWindowIcon(icon)
		self.Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
		
		self.label = QtWidgets.QLabel(self.Dialog)
		self.label.setGeometry(QtCore.QRect(20, 20, 61, 21))
		self.label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setOpenExternalLinks(False)
		self.label.setObjectName("label")
		self.youtube_title = QtWidgets.QLabel(self.Dialog)
		self.youtube_title.setGeometry(QtCore.QRect(100, 20, 391, 21))
		self.youtube_title.setObjectName("youtube_title")
		self.label_2 = QtWidgets.QLabel(self.Dialog)
		self.label_2.setGeometry(QtCore.QRect(20, 60, 61, 21))
		self.label_2.setObjectName("label_2")
		self.channel_name = QtWidgets.QLabel(self.Dialog)
		self.channel_name.setGeometry(QtCore.QRect(100, 60, 391, 21))
		self.channel_name.setObjectName("channel_name")
		self.label_4 = QtWidgets.QLabel(self.Dialog)
		self.label_4.setGeometry(QtCore.QRect(20, 100, 61, 21))
		self.label_4.setAlignment(QtCore.Qt.AlignCenter)
		self.label_4.setObjectName("label_4")
		self.view_count = QtWidgets.QLabel(self.Dialog)
		self.view_count.setGeometry(QtCore.QRect(100, 100, 191, 21))
		self.view_count.setObjectName("view_count")
		self.label_6 = QtWidgets.QLabel(self.Dialog)
		self.label_6.setGeometry(QtCore.QRect(20, 140, 61, 21))
		self.label_6.setAlignment(QtCore.Qt.AlignCenter)
		self.label_6.setObjectName("label_6")
		self.likes = QtWidgets.QLabel(self.Dialog)
		self.likes.setGeometry(QtCore.QRect(100, 140, 91, 21))
		self.likes.setObjectName("likes")
		self.label_8 = QtWidgets.QLabel(self.Dialog)
		self.label_8.setGeometry(QtCore.QRect(220, 140, 61, 21))
		self.label_8.setAlignment(QtCore.Qt.AlignCenter)
		self.label_8.setObjectName("label_8")
		self.dislikes = QtWidgets.QLabel(self.Dialog)
		self.dislikes.setGeometry(QtCore.QRect(300, 140, 91, 21))
		self.dislikes.setObjectName("dislikes")
		self.textBrowser = QtWidgets.QTextBrowser(self.Dialog)
		self.textBrowser.setGeometry(QtCore.QRect(50, 190, 371, 31))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.textBrowser.setFont(font)
		self.textBrowser.setFocusPolicy(QtCore.Qt.NoFocus)
		self.textBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
		self.textBrowser.setObjectName("textBrowser")
		self.save = QtWidgets.QPushButton(self.Dialog)
		self.save.setGeometry(QtCore.QRect(440, 190, 41, 31))
		self.save.setFocusPolicy(QtCore.Qt.NoFocus)
		self.save.setText("")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("click.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.save.setIcon(icon1)
		self.save.setIconSize(QtCore.QSize(30, 30))
		self.save.setObjectName("save")
		self.comboBox = QtWidgets.QComboBox(self.Dialog)
		self.comboBox.setGeometry(QtCore.QRect(150, 260, 231, 21))
		self.comboBox.setObjectName("comboBox")
		self.label_7 = QtWidgets.QLabel(self.Dialog)
		self.label_7.setGeometry(QtCore.QRect(30, 250, 111, 41))
		self.label_7.setAlignment(QtCore.Qt.AlignCenter)
		self.label_7.setObjectName("label_7")
		self.progressBar = QtWidgets.QProgressBar(self.Dialog)
		self.progressBar.setGeometry(QtCore.QRect(30, 310, 481, 23))
		self.progressBar.setProperty("value", 0)
		self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
		self.progressBar.setObjectName("progressBar")
		self.pushButton = QtWidgets.QPushButton(self.Dialog)
		self.pushButton.setGeometry(QtCore.QRect(170, 370, 201, 31))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.pushButton.setFont(font)
		self.pushButton.setObjectName("pushButton")

		self.audio = pafy.new(self.you.page().requestedUrl().toString())

		self.youtube_title.setText(self.audio.title)
		self.youtube_title.adjustSize()

		self.channel_name.setText(self.audio.author)
		self.channel_name.adjustSize()

		self.view_count.setText(str(self.audio.viewcount))
		self.view_count.adjustSize()

		self.likes.setText(str(self.audio.likes))
		self.likes.adjustSize()

		self.dislikes.setText(str(self.audio.dislikes))
		self.dislikes.adjustSize()

		self.combo = []
		data = self.get_audio_data()
		self.comboBox.addItems(data)
		self.save.clicked.connect(self.save_location)
		thumbnail = self.audio.bigthumbhd
		print(thumbnail)
		r = requests.get(thumbnail, allow_redirects=True)
		open('thumbnail.jpg', 'wb').write(r.content)
		self.pushButton.clicked.connect(self.download_aud)

		# self.Dialog.adjustSize()
		self.Dialog.setFixedSize(self.Dialog.size())
		self.Dialog.show()

		self.retranslateUi_Dialoga(self.Dialog)
		QtCore.QMetaObject.connectSlotsByName(self.Dialog)

	def retranslateUi_Dialoga(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		self.Dialog.setWindowTitle(_translate("self.Dialog", "Download Audio"))
		self.label.setText(_translate("self.Dialog", "TITLE :-"))
		# self.youtube_title.setText(_translate("self.Dialog", "YOUTUBE TITLE"))
		self.label_2.setText(_translate("self.Dialog", "CHANNEL :-"))
		# self.channel_name.setText(_translate("self.Dialog", "CHANNEL NAME"))
		self.label_4.setText(_translate("self.Dialog", "VIEWS :-"))
		# self.view_count.setText(_translate("self.Dialog", "VIEWS"))
		self.label_6.setText(_translate("self.Dialog", "LIKES :-"))
		# self.likes.setText(_translate("self.Dialog", "LIKE_NO"))
		self.label_8.setText(_translate("self.Dialog", "DISLIKES:-"))
		# self.dislikes.setText(_translate("self.Dialog", "DISLIKE_NO"))
		self.textBrowser.setPlaceholderText(_translate("self.Dialog", "Click the button to choose a folder."))
		self.label_7.setText(_translate("self.Dialog", "Select Quality :-"))
		self.progressBar.setFormat(_translate("self.Dialog", "%p%"))
		self.pushButton.setText(_translate("self.Dialog", "Download"))

	def download(self):
		self.rownumber += 1
		quality = self.comboBox.currentIndex()
		storage = self.textBrowser.toPlainText()
		vid_stream = self.video.videostreams
		aud_stream = self.video.audiostreams
		if storage == '':
			QtWidgets.QMessageBox.warning(self.Dialog, "Data Error", "Select a proper folder..")
		else:
			# vid_stream[quality].download(filepath=storage, callback=self.progress)
			vid_stream[quality].download(callback=self.progress)
			# aud_stream[-1].download(filepath=storage)
			aud_stream[-1].download()
			title = self.video.title
			if storage.find("/") != -1:
				storage = storage.replace("/", r"\\")
			if title.find("|") != -1:
				title = self.video.title.replace("|", "_")
			video_file = title + "." + vid_stream[quality].extension
			audio_file = title + "." + aud_stream[-1].extension
			print(video_file)
			print(audio_file)
			direct = os.getcwd()
			time.sleep(0.2)
			video = VideoFileClip(video_file)
			audio = AudioFileClip(audio_file)
			self.progressBar.setValue(88)
			final = video.set_audio(audio)
			final.write_videofile("output.mp4", bitrate='3000k')
			imput = str(direct + r"\\output.mp4")
			output = str(storage + r"\\" + title + ".mp4")
			shutil.move(imput, output)
			os.remove(video_file)
			os.remove(audio_file)
			time.sleep(0.8)
			self.progressBar.setValue(100)
			time.sleep(2)
			QtWidgets.QMessageBox.information(self.Dialog, "Download Video", " Download complete !! ")
			self.Dialog.close()
			self.tableWidget.setRowCount(self.rownumber)
			self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
			item = QtWidgets.QTableWidgetItem(self.video.title)
			item.setTextAlignment(4)
			self.tableWidget.setItem(self.rownumber - 1, 0, item)
			item = QtWidgets.QTableWidgetItem("Video")
			item.setTextAlignment(4)
			self.tableWidget.setItem(self.rownumber - 1, 1, item)
			item = QtWidgets.QTableWidgetItem(self.size)
			item.setTextAlignment(4)
			self.tableWidget.setItem(self.rownumber - 1, 2, item)

	def download_aud(self):
		self.rownumber += 1
		quality = self.comboBox.currentIndex()
		storage = self.textBrowser.toPlainText()
		stream = self.audio.audiostreams
		if storage == '':
			QtWidgets.QMessageBox.warning(self.Dialog, "Data Error", "Select a proper folder..")
		else:
			stream[quality].download(callback=self.progress)
			title = self.audio.title
			if title.find("/") != -1:
				title = title.replace("/", r"\\")
			if title.find("|") != -1:
				title = self.audio.title.replace("|", "_")
			elif title.find(" | ") != -1:
				title = self.audio.title.replace("|", "_")
			audio_ext = title + "." + stream[quality].extension
			thumb_ext = "thumbnail.jpg"
			direct = os.getcwd()
			audio_down = str(direct + r"/" + audio_ext)
			thumb_file = str(direct + r"/" + thumb_ext)
			audio_file = str(direct + r"/output.mp3")
			os.rename(audio_down, audio_file)
			# audio = MP3(audio_file, ID3=ID3)
			# # adding ID3 tag if it is not present
			# try:
			# 	audio.add_tags()
			# except error:
			# 	pass
			# audio.tags.add(APIC(mime='image/jpeg',type=3,desc=u'Cover',data=open(thumb_file,'rb').read()))
			# audio.save()
			time.sleep(2)
			QtWidgets.QMessageBox.information(self.Dialog, "Download Audio", " Download complete !! ")
			self.Dialog.close()
			self.tableWidget.setRowCount(self.rownumber)
			self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
			item = QtWidgets.QTableWidgetItem(self.audio.title)
			item.setTextAlignment(4)
			self.tableWidget.setItem(self.rownumber - 1, 0, item)
			item = QtWidgets.QTableWidgetItem("Audio")
			item.setTextAlignment(4)
			self.tableWidget.setItem(self.rownumber - 1, 1, item)
			item = QtWidgets.QTableWidgetItem(self.size)
			item.setTextAlignment(4)
			self.tableWidget.setItem(self.rownumber - 1, 2, item)

	def progress(self, total, received, ratio, rate, times):
		read = received
		if total > 0:
			download_percentage = read * 100 / total
			if download_percentage > 80:
				self.progressBar.setValue(80)
			else:
				self.progressBar.setValue(download_percentage)
		self.size = humanize.naturalsize(total)

	def go_to(self):
		link = self.urltext.text()
		if link == '':
			return
		else:
			if link.find("watch?") != -1:
				self.you.load(QtCore.QUrl(link))
				self.you.showFullScreen()
				self.you.adjustSize()
			elif link.find("youtube.com") != -1:
				self.web.load(QtCore.QUrl(link))
			elif link.find("http") != -1 or link.find("https") != -1:
				QtWidgets.QMessageBox.information(self.centralwidget, "Data Error", "The link given is not valid for "
																					"this application!! ")
			else:
				return

	def lab(self):
		current = self.web.page().requestedUrl().toString()
		print(current)
		if current.find("watch?") != -1:
			self.web.hide()
			print("watchable")
			self.you.load(QtCore.QUrl(current))
			self.you.showFullScreen()
			self.you.adjustSize()
			self.DownloadVideo.setEnabled(True)
			self.DownloadAudio.setEnabled(True)
		else:
			return

	def retranslateUi(self, mainWindow):
		_translate = QtCore.QCoreApplication.translate
		mainWindow.setWindowTitle(_translate("mainWindow", "Youtube Downloader 2.0"))
		item = self.tableWidget.horizontalHeaderItem(0)
		item.setText(_translate("mainWindow", "Name"))
		item = self.tableWidget.horizontalHeaderItem(1)
		item.setText(_translate("mainWindow", "Type"))
		item = self.tableWidget.horizontalHeaderItem(2)
		item.setText(_translate("mainWindow", "Size"))
		item = self.tableWidget.horizontalHeaderItem(3)
		item.setText(_translate("mainWindow", "Progress"))
		item = self.tableWidget.horizontalHeaderItem(4)
		item.setText(_translate("mainWindow", "Download speed"))
		item = self.tableWidget.horizontalHeaderItem(5)
		item.setText(_translate("mainWindow", "Date Modified"))
		self.pushBack.setStatusTip(_translate("mainWindow", "Go back"))
		self.pushplay.setStatusTip(_translate("mainWindow", "Play and Pause"))
		self.pushnext.setStatusTip(_translate("mainWindow", "Go forward"))
		self.DownloadVideo.setStatusTip(_translate("mainWindow", "Download Video"))
		self.DownloadAudio.setStatusTip(_translate("mainWindow", "Download Audio"))
		self.webpageback.setStatusTip(_translate("mainWindow", "Move back"))
		self.webpagefront.setStatusTip(_translate("mainWindow", "Move forward"))
		self.webpagerefresh.setStatusTip(_translate("mainWindow", "Refresh page"))
		self.webpagelabel.setText(_translate("mainWindow", "www.YouTube.com"))
		self.urltext.setStatusTip(_translate("mainWindow", "Enter the url of YouTube video"))
		self.urltext.setPlaceholderText(_translate("mainWindow", "Enter the url of YouTube video"))
		self.searchbutton.setStatusTip(_translate("mainWindow", "Search video"))
		self.searchbutton.setShortcut(_translate("mainWindow", "Return"))
		self.menuFile.setTitle(_translate("mainWindow", "File"))
		self.menuEdit.setTitle(_translate("mainWindow", "Edit"))
		self.menuHelp.setTitle(_translate("mainWindow", "Help"))
		self.menuTools.setTitle(_translate("mainWindow", "Tools"))
		self.actionNew.setText(_translate("mainWindow", "New"))
		self.actionNew.setStatusTip(_translate("mainWindow", "Create a new window"))
		self.actionNew.setShortcut(_translate("mainWindow", "Ctrl+N"))
		self.actionOpen.setText(_translate("mainWindow", "Open"))
		self.actionOpen.setStatusTip(_translate("mainWindow", "Open a file"))
		self.actionOpen.setShortcut(_translate("mainWindow", "Ctrl+O"))
		self.actionSave.setText(_translate("mainWindow", "Save"))
		self.actionSave.setStatusTip(_translate("mainWindow", "Save a file"))
		self.actionSave.setShortcut(_translate("mainWindow", "Ctrl+S"))
		self.actionSave_As.setText(_translate("mainWindow", "Save As"))
		self.actionSave_As.setStatusTip(_translate("mainWindow", "Save As"))
		self.actionConsole.setText(_translate("mainWindow", "Console"))
		self.actionConsole.setStatusTip(_translate("mainWindow", "Open the console"))
		self.actionConsole.setShortcut(_translate("mainWindow", "Ctrl+Alt+T"))
		self.actionExit.setText(_translate("mainWindow", "Exit"))
		self.actionExit.setStatusTip(_translate("mainWindow", "Exit the app"))
		self.actionExit.setShortcut(_translate("mainWindow", "Ctrl+Q"))
		self.actionCopy.setText(_translate("mainWindow", "Copy"))
		self.actionCopy.setStatusTip(_translate("mainWindow", "Copy the file"))
		self.actionCopy.setShortcut(_translate("mainWindow", "Ctrl+C"))
		self.actionPaste.setText(_translate("mainWindow", "Paste"))
		self.actionPaste.setStatusTip(_translate("mainWindow", "Paste the file"))
		self.actionPaste.setShortcut(_translate("mainWindow", "Ctrl+V"))
		self.actionCut.setText(_translate("mainWindow", "Cut"))
		self.actionCut.setStatusTip(_translate("mainWindow", "Cut the file permanently move to another place"))
		self.actionCut.setShortcut(_translate("mainWindow", "Ctrl+X"))
		self.actionAbout_Youtube_Downloader.setText(_translate("mainWindow", "About Youtube Downloader"))
		self.actionHow_to_Download.setText(_translate("mainWindow", "How to download Video"))
		self.actionHow_to_download_Audio.setText(_translate("mainWindow", "How to download Audio"))
		self.actionConvert_to_mp3.setText(_translate("mainWindow", "Convert to .mp3"))
		self.actionConvert_to_mp3.setStatusTip(_translate("mainWindow", "Convert a video file to .mp3"))
		self.actionSpeed_Test.setText(_translate("mainWindow", "Speed Test"))
		self.actionSpeed_Test.setStatusTip(_translate("mainWindow", "Check your internet speed"))


if __name__ == "__main__":
	import sys

	app = QtWidgets.QApplication(sys.argv)
	mainWindow = QtWidgets.QMainWindow()
	ui = Ui_mainWindow()
	ui.setupUi(mainWindow)
	mainWindow.show()
	sys.exit(app.exec_())
