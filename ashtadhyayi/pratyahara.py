#!/usr/bin/env python3
# -*- coding: utf-8 -*-


प्रत्याहारसूत्राणि = [
                'अइउण्',
                'ऋऌक्',
                'एओङ्',
                'ऐऔच्',
                'हयवरट्',
                'लण्',
                'ञमङणनम्',
                'झभञ्',
                'घढधष्',
                'जबगडदश्',
                'खफछठथचटतव्',
                'कपय्',
                'शषसर्',
                'हल्']


def वर्णाः(प्रत्याहारः, द्वितीयः=False):
    वर्णाः = []
    for प्रत्याहारसूत्र in प्रत्याहारसूत्राणि:
        # प्रत्याहारः[0] is the start. -2 for अनुबन्धः
        try:
            if not वर्णाः:
                वर्णाः = प्रत्याहारसूत्र[(प्रत्याहारसूत्र.index(प्रत्याहारः[0])): -2]
            else:
                वर्णाः += प्रत्याहारसूत्र[:-2]

            if प्रत्याहारसूत्र[-2:] == प्रत्याहारः[-2:]:
                if द्वितीयः:
                    द्वितीयः = False
                else:
                    break
        except ValueError:
            continue

    return वर्णाः


def वल्(वर्ण):
    return वर्ण in वर्णाः('वल्')


def इक्(वर्ण):
    return वर्ण in वर्णाः('इक्')


def हल्(वर्ण):
    return वर्ण in वर्णाः('हल्')


def अच्(वर्ण):
    return वर्ण in वर्णाः('अच्')

# with open('ashtadhyayi/pratyaharas.txt') as f:
#     pratyaharas = f.readlines()

# w = open('ashtadhyayi/pratyahara_ouput.txt', 'w')

# w.writelines([pratyahara[:-1] + ' '+ वर्णाः(pratyahara[:-1]) +'\n' for pratyahara in pratyaharas])
