# coding=utf-8
__author__ = 'agr'

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint


class SeriesDescription():
    titleRus = ""
    description = ""
    title = ""
    genre = ""
    country = ""
    year = 1900
    director = ""
    roles = []


class MyHTMLParser(HTMLParser):
    TITLE_RUS = "TITLE_RUS"
    DESCRIPTION = "DESCRIPTION"
    TITLE = "TITLE"
    GENRE = "GENRE"
    COUNTRY = "COUNTRY"
    YEAR = "YEAR"
    DIRECTOR = "DIRECTOR"
    ROLES = "ROLES"

    CONCRETE_PLACE = ""
    attribute = ""
    dataLoaded = "false"

    seriesDescription = SeriesDescription()

    def handel_attrs(self, attrs):
        for attr in attrs:
            self.attribute = attr


    def handle_starttag(self, tag, attrs):
        print "Start tag:", tag
        self.handel_attrs(attrs)
        if self.attribute[0] == "class" and self.attribute[1] == "hname" and self.CONCRETE_PLACE == "":
            self.CONCRETE_PLACE = self.TITLE_RUS
            self.dataLoaded = "false"
        if tag == "p" and self.CONCRETE_PLACE == self.TITLE_RUS:
            self.CONCRETE_PLACE = self.DESCRIPTION
            self.dataLoaded = "false"
        if tag == "span" and self.attribute[0] == "class" and self.attribute[1] == "videl":
            if self.CONCRETE_PLACE == self.DESCRIPTION:
                self.CONCRETE_PLACE = self.TITLE
            elif self.CONCRETE_PLACE == self.TITLE:
                self.CONCRETE_PLACE = self.GENRE
            elif self.CONCRETE_PLACE == self.GENRE:
                self.CONCRETE_PLACE = self.COUNTRY
            elif self.CONCRETE_PLACE == self.COUNTRY:
                self.CONCRETE_PLACE = self.YEAR
            elif self.CONCRETE_PLACE == self.YEAR:
                self.CONCRETE_PLACE = self.DIRECTOR
            elif self.CONCRETE_PLACE == self.DIRECTOR:
                self.CONCRETE_PLACE = self.ROLES
        if tag == "a" and self.CONCRETE_PLACE == self.ROLES:
            self.dataLoaded = "false"

    def handle_endtag(self, tag):
        print "End tag  :", tag
        if tag == "span" and self.CONCRETE_PLACE == self.TITLE:
            self.dataLoaded = "false"
        if tag == "span" and self.CONCRETE_PLACE == self.GENRE:
            self.dataLoaded = "false"
        if tag == "span" and self.CONCRETE_PLACE == self.COUNTRY:
            self.dataLoaded = "false"
        if tag == "span" and self.CONCRETE_PLACE == self.YEAR:
            self.dataLoaded = "false"
        if tag == "span" and self.CONCRETE_PLACE == self.DIRECTOR:
            self.dataLoaded = "false"
        if tag == "span" and self.CONCRETE_PLACE == self.ROLES:
            self.dataLoaded = "false"

    def handle_data(self, data):
        print "Data     :", data
        if self.CONCRETE_PLACE == self.TITLE_RUS and self.dataLoaded == "false":
            print "Data for TITLE_RUS is %s " % data
            self.seriesDescription.titleRus = data
            self.dataLoaded = "true"
        if self.CONCRETE_PLACE == self.DESCRIPTION and self.dataLoaded == "false":
            print "Data for DESCRIPTION is %s " % data
            self.seriesDescription.description = data
            self.dataLoaded = "true"
        if self.CONCRETE_PLACE == self.TITLE and self.dataLoaded == "false":
            print "Data for TITLE is %s " % data
            self.seriesDescription.title = data
            self.dataLoaded = "true"
        if self.CONCRETE_PLACE == self.GENRE and self.dataLoaded == "false":
            print "Data for GENRE is %s " % data
            self.seriesDescription.genre = data
            self.dataLoaded = "true"
        if self.CONCRETE_PLACE == self.COUNTRY and self.dataLoaded == "false":
            print "Data for COUNTRY is %s " % data
            self.seriesDescription.country = data
            self.dataLoaded = "true"
        if self.CONCRETE_PLACE == self.YEAR and self.dataLoaded == "false":
            print "Data for YEAR is %s " % data
            self.seriesDescription.year = data
            self.dataLoaded = "true"
        if self.CONCRETE_PLACE == self.DIRECTOR and self.dataLoaded == "false":
            print "Data for DIRECTOR is %s " % data
            self.seriesDescription.director = data
            self.dataLoaded = "true"
        if self.CONCRETE_PLACE == self.ROLES and self.dataLoaded == "false":
            print "Data for ROLES is %s " % data
            self.seriesDescription.roles.append(data)
            print self.seriesDescription
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