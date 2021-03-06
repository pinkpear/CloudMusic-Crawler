#!/usr/bin/env python3

import data_handler as dh
import api_simple as api
from pprint import pprint
import json


def test_get_music_comments():
	comments = api.get_music_comments(25906124, offset=0, total='true', limit=100)
	for comment in comments['comments']:
		print(comment['user']['nickname']+'\n'+'-'*25+'\n'+comment['content']+'\n')
		if comment['beReplied']:
			for replied in comment['beReplied']:
				print('======>'+replied['user']['nickname'])
				print(replied['content']+'\n')


def test_get_artists_from_file():
	a = dh.get_artists_from_file('./data/artists_list.txt')
	print(a['大乔小乔'])


def test_get_lyrics_from_artists_list():
	b = dh.get_artists_from_playlist(881367835)
	print(b['陈奕迅'])


def test_get_lyrics_from_artist_id():
	c = dh.get_lyrics_from_artist_id(2116)
	pprint(c)


def test_purify_lyric_text():
	lyric = ('[by:Taynochan]\n[ti:不要说话]\n[ar:陈奕迅]\n[al:博儿Lrc试练]\n[by:博儿]\n'
		'[00:00.00] 作曲 : 小柯\n[00:01.00] 作词 : 小柯 \u3000\u3000\n[00:18.77]深色的'
		'海面布满白色的月光\n[00:24.51]\n[00:25.11]我出神望着海 心不知飞哪去\n[00:31.64]听'
		'到他在告诉你\n[00:35.28]说他真的喜欢你\n[00:39.48]我不知该 躲哪里\n[00:47.17]爱一'
		'个人是不是应该有默契\n[00:54.15]我以为你懂得每当我看着你\n[01:00.07]我藏起来的秘密\n'
		'[01:03.67]在每一天清晨里\n[01:07.60]暖成咖啡 安静的拿给你\n[01:14.33]愿意 用一支黑色的铅笔\n'
		'[01:18.81]画一出沉默舞台剧\n[01:22.95]灯光再亮 也抱住你\n[01:28.53]愿意 在角落唱沙哑的歌\n'
		'[01:33.06]再大声也都是给你\n[01:37.24]请用心听 不要说话\n[01:51.54]爱一个人是不是应该要默契\n'
		'[01:58.36]我以为你懂得每当我看着你\n[02:04.34]我藏起来的秘密\n[02:08.22]在每一天清晨里\n[02:11.47]'
		'暖成咖啡 安静的拿给你\n[02:18.49]愿意 用一支黑色的铅笔\n[02:22.92]画一出沉默舞台剧\n[02:27.31]'
		'灯光再亮 也抱住你\n[02:33.04]愿意 在角落唱沙哑的歌\n[02:37.33]再大声也都是给你\n[02:41.46]请用心听'
		' 不要说话\n[03:15.81]愿意 用一支黑色的铅笔\n[03:19.95]画一出沉默舞台剧\n[03:24.43]灯光再亮'
		' 也抱住你\n[03:29.82]愿意 在角落唱沙哑的歌\n[03:34.19]再大声也都是给你\n[03:38.48]请原谅我'
		' 不会说谎\n[03:44.11]愿意 用一支黑色的铅笔\n[03:48.55]画一出沉默舞台剧\n[03:52.68]灯光再亮'
		' 也抱住你\n[03:58.35]愿意 在角落唱沙哑的歌\n[04:02.84]再大声也都是给你\n[04:06.97]爱是用心吗'
		' 不要说话\n')

	text = dh.purify_lyric_text(lyric, 0)
	pprint(text)


def test_get_lyrics_from_artists_list():
	artists_list = dh.get_artists_from_file('./data/artists_list.txt')
	# artists_list = get_artists_from_playlist()
	dh.get_lyrics_from_artists_list(artists_list)


def test_json_data_format():
	with open('./data/lyrics.json', 'r') as f:
		data = json.load(f)
	pprint(data)

def test_comments_handler():
	comments = dh.comments_handler(460685960)
	
	pprint(comments)
	
	# with open('./data/test.json', 'w') as f:
	# 	json.dump(comments, f)


if __name__ == '__main__':
	test_comments_handler()
