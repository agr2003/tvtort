# coding=utf-8
__author__ = 'agr'

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):

    TITLE_RUS = "TITLE_RUS"
    DESCRIPTION = "DESCRIPTION"
    TITLE = "TITLE"
    GENRE = "GENRE"
    COUNTRY = "COUNTRY"
    YEAR = "YEAR"
    DIRECTOR = "DIRECTOR"
    ROLES = "ROLES"

    TITLE_NAME = "Оригинал:"
    GENRE_NAME = "Жанр:"
    COUNTRY_NAME = "Страна:"
    YEAR_NAME = "Вышел:"
    DIRECTOR_NAME = "Режиссер:"
    ROLES_NAME = "Роли:"

    CONCRETE_PLACE = ""
    attribute = ""
    dataLoaded = "false"

    def handel_attrs(self, attrs):
        for attr in attrs:
            self.attribute = attr


    def handle_starttag(self, tag, attrs):
        print "Start tag:", tag
        self.handel_attrs(attrs)
        if self.attribute[0] == "class" and self.attribute[1] == "hname" and self.CONCRETE_PLACE == "" :
            self.CONCRETE_PLACE = self.TITLE_RUS
            self.dataLoaded = "false"
        if tag == "p" and self.CONCRETE_PLACE == self.TITLE_RUS:
            self.CONCRETE_PLACE = self.DESCRIPTION
            self.dataLoaded = "false"
        if tag == "span" and self.attribute[0]=="class" and self.attribute[1]=="videl" and self.CONCRETE_PLACE == self.DESCRIPTION:
            self.CONCRETE_PLACE = self.TITLE
            self.dataLoaded = "false"


    def handle_endtag(self, tag):
        print "End tag  :", tag
    def handle_data(self, data):
        print "Data     :", data
        if self.CONCRETE_PLACE == self.TITLE_RUS and self.dataLoaded == "false":
            print "Data for TITLE_RUS is %s " % data
            self.dataLoaded = "true"
        if self.CONCRETE_PLACE == self.DESCRIPTION and self.dataLoaded == "false":
            print "Data for DESCRIPTION is %s " % data
            self.dataLoaded = "true"
        if self.CONCRETE_PLACE == self.TITLE and self.dataLoaded == "false":
            print "Data for TITLE is %s " % data
            self.dataLoaded = "true"


    def handle_comment(self, data):
        print "Comment  :", data
    def handle_entityref(self, name):
        c = unichr(name2codepoint[name])
        print "Named ent:", c
    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        print "Num ent  :", c
    def handle_decl(self, data):
        print "Decl     :", data

parser = MyHTMLParser()

parser.feed(open("htmlExample.html", "r").read())