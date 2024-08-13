import pyautogui
import time

import re

# The XML content as a string
xml_content = '''<outline text="下一本讀什麼？" type="rss" xmlUrl="https://feed.firstory.me/rss/user/cl39lz2ky01co01ugaba7gr9y"  htmlUrl="https://open.firstory.me/user/readingoutpost" />
<outline text="Global News Podcast" type="rss" xmlUrl="https://podcasts.files.bbci.co.uk/p02nq0gn.rss"  htmlUrl="http://www.bbc.co.uk/programmes/p02nq0gn" />
<outline text="百靈果 News" type="rss" xmlUrl="https://feeds.buzzsprout.com/1974862.rss"  htmlUrl="https://www.bailingguonews.com" />
<outline text="共時好生活" type="rss" xmlUrl="https://feeds.soundon.fm/podcasts/7da9f2bf-fb4d-4f20-9a73-36579514a0c3.xml"  htmlUrl="https://www.facebook.com/LancasterTien/" />
<outline text="Motivation Daily by Motiversity" type="rss" xmlUrl="https://feeds.acast.com/public/shows/6114541c545d640012cfb625"  htmlUrl="https://motiversity.com" />
<outline text="Pod Save America" type="rss" xmlUrl="https://feeds.simplecast.com/dxZsm5kX"  htmlUrl="https://crooked.com" />
<outline text="Ten Percent Happier with Dan Harris" type="rss" xmlUrl="https://rss.art19.com/ten-percent-happier"  htmlUrl="https://www.tenpercent.com/podcast" />
<outline text="Wow in the World" type="rss" xmlUrl="https://rss.art19.com/wow-in-the-world"  htmlUrl="https://wondery.com/shows/wow-in-the-world/?utm_source=rss" />
<outline text="啟點文化一天聽一點" type="rss" xmlUrl="https://feeds.soundcloud.com/users/soundcloud:users:737120962/sounds.rss"  htmlUrl="https://www.koob.com.tw/" />
<outline text="No Stupid Questions" type="rss" xmlUrl="https://feeds.simplecast.com/dfh_verV"  htmlUrl="https://freakonomics.com" />
<outline text="今周大耳朵" type="rss" xmlUrl="https://feeds.soundon.fm/podcasts/0d428b4f-0cf3-44ad-a7ce-f6b359da55b9.xml"  htmlUrl="https://player.soundon.fm/p/0d428b4f-0cf3-44ad-a7ce-f6b359da55b9" />
<outline text="Sleep Meditation for Women" type="rss" xmlUrl="https://feeds.megaphone.fm/sleepmeditationforwomen"  htmlUrl="http://womensmeditationnetwork.com" />
<outline text="The Sleepy Bookshelf" type="rss" xmlUrl="https://feeds.simplecast.com/x7Iwqf_H"  htmlUrl="https://sleepybookshelf.com/" />
<outline text="All In The Mind" type="rss" xmlUrl="https://www.abc.net.au/feeds/2888650/podcast.xml"  htmlUrl="https://www.abc.net.au/listen/programs/allinthemind/" />
<outline text="TED Talks Daily" type="rss" xmlUrl="https://feeds.feedburner.com/tedtalks_audio"  htmlUrl="https://www.ted.com/talks" />
<outline text="InvestTalk" type="rss" xmlUrl="https://feeds.redcircle.com/6fb1e853-719d-44d9-8b9e-9d4af81d7a89"  htmlUrl="https://redcircle.com/shows/investtalk-investment-in-stock-market-financial-planning" />
<outline text="Planet Money" type="rss" xmlUrl="https://feeds.npr.org/510289/podcast.xml"  htmlUrl="https://www.npr.org/podcasts/510289/planet-money" />
<outline text="The Indicator from Planet Money" type="rss" xmlUrl="https://feeds.npr.org/510325/podcast.xml"  htmlUrl="https://www.npr.org/podcasts/510325/the-indicator-from-planet-money" />
<outline text="Insight Hour with Joseph Goldstein" type="rss" xmlUrl="https://rss.art19.com/insight-hour-with-joseph-goldstein"  htmlUrl="https://art19.com/shows/insight-hour-with-joseph-goldstein" />
<outline text="No Bad Dogs Podcast" type="rss" xmlUrl="https://feeds.redcircle.com/b12edd38-fb43-4c65-b829-e900502f38a3"  htmlUrl="https://redcircle.com/shows/no-bad-dogs-podcast" />
<outline text="K歌Su房" type="rss" xmlUrl="https://feeds.buzzsprout.com/2032433.rss"  htmlUrl="https://www.buzzsprout.com/2032433" />
<outline text="Radiolab" type="rss" xmlUrl="https://feeds.simplecast.com/EmVW7VGp"  htmlUrl="https://www.wnycstudios.org/podcasts/radiolab/projects/podcasts" />
<outline text="Ideas" type="rss" xmlUrl="https://www.cbc.ca/podcasting/includes/ideas.xml"  htmlUrl="https://www.cbc.ca/radio/ideas" />
<outline text="Personality Hacker Podcast" type="rss" xmlUrl="https://personalityhacker.libsyn.com/rss"  htmlUrl="https://personalityhacker.com" />
<outline text="馬力歐陪你喝一杯" type="rss" xmlUrl="https://www.omnycontent.com/d/playlist/a4cc0a4a-642d-45d7-ac5d-ac5600c620b0/1d06778d-ee1a-4d81-882e-ac9a00368a17/b7a04983-22ba-406b-b1c4-ac9a00368a25/podcast.rss"  htmlUrl="http://drinkwithmario.thenewslens.com/" />
<outline text="TED Radio Hour" type="rss" xmlUrl="https://feeds.npr.org/510298/podcast.xml"  htmlUrl="https://www.npr.org/podcasts/510298/ted-radio-hour" />
<outline text="On Purpose with Jay Shetty" type="rss" xmlUrl="https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/32f1779e-bc01-4d36-89e6-afcb01070c82/e0c8382f-48d4-42bb-89d5-afcb01075cb4/podcast.rss"  htmlUrl="https://www.iheart.com/podcast/867-on-purpose-with-jay-shetty-30589432/" />
<outline text="The Diary Of A CEO with Steven Bartlett" type="rss" xmlUrl="https://feeds.megaphone.fm/thediaryofaceo"  htmlUrl="https://podcasters.spotify.com/pod/show/thediaryofaceo" />
<outline text="轉吧！創夢大叔" type="rss" xmlUrl="https://feeds.soundon.fm/podcasts/938c2ef7-9948-4f1d-9d96-9acc18527c68.xml"  htmlUrl="https://player.soundon.fm/p/938c2ef7-9948-4f1d-9d96-9acc18527c68" />
<outline text="Snap Judgment" type="rss" xmlUrl="https://snap.feed.snapjudgment.org"  htmlUrl="http://snapjudgment.org/" />
<outline text="Critical Role" type="rss" xmlUrl="https://feeds.simplecast.com/LXz4Q9rJ"  htmlUrl="https://www.stitcher.com" />
<outline text="劉軒的How to人生學" type="rss" xmlUrl="https://feeds.soundon.fm/podcasts/17e025f5-3a87-41b5-8cff-af804ad195f3.xml"  htmlUrl="https://www.soundshine.com.tw/podcast-how-to-life/" />
<outline text="Software Engineering Daily" type="rss" xmlUrl="https://softwareengineeringdaily.com/feed/podcast/"  htmlUrl="https://softwareengineeringdaily.com/" />
<outline text="The Next Big Idea" type="rss" xmlUrl="https://feeds.megaphone.fm/LI1683199352"  htmlUrl="https://nextbigideaclub.com/" />
<outline text="How I Built This with Guy Raz" type="rss" xmlUrl="https://rss.art19.com/how-i-built-this"  htmlUrl="https://wondery.com/shows/how-i-built-this/?utm_source=rss" />
<outline text="The Psychology Podcast" type="rss" xmlUrl="https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/47e6a3a1-adc4-4e4e-9a7a-b09d01547555/80fe8468-f75f-485a-8023-b09d0154757b/podcast.rss"  htmlUrl="https://www.iheart.com/podcast/1119-the-psychology-podcast-96239856" />
<outline text="Throughline" type="rss" xmlUrl="https://feeds.npr.org/510333/podcast.xml"  htmlUrl="https://www.npr.org/podcasts/510333/throughline" />
<outline text="Behind the Review" type="rss" xmlUrl="https://behindthereview.libsyn.com/rss"  htmlUrl="https://www.entrepreneur.com/listen/behind-the-review" />
<outline text="Nothing much happens: bedtime stories to help you sleep" type="rss" xmlUrl="https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/a1a8ed4e-0091-4802-a9ad-afff01499406/2d8fbaf5-80f0-4d52-bcb7-afff014a92f0/podcast.rss"  htmlUrl="https://www.iheart.com/podcast/263-nothing-much-happen-29945275/" />
<outline text="Freakonomics Radio" type="rss" xmlUrl="https://feeds.simplecast.com/Y8lFbOT4"  htmlUrl="https://freakonomics.com" />
<outline text="Guided Sleep Meditation &amp; Sleep Hypnosis from Sleep Cove" type="rss" xmlUrl="https://feeds.megaphone.fm/ARML2818067425"  htmlUrl="https://www.sleepcove.com" />
<outline text="哇賽心理學" type="rss" xmlUrl="https://feed.firstory.me/rss/user/ck7t2fz77qu7g0873ln5hz5cl"  htmlUrl="https://onyourpsy.firstory.io" />
<outline text="大人的Small Talk" type="rss" xmlUrl="https://feeds.soundon.fm/podcasts/6731d283-54f0-49ec-a040-e5a641c3125f.xml"  htmlUrl="https://www.darencademy.com/" />
<outline text="Sleep With Me" type="rss" xmlUrl="https://feed.sleepwithmepodcast.com/"  htmlUrl="http://www.sleepwithmepodcast.com" />
<outline text="Get Sleepy: Sleep meditation and stories" type="rss" xmlUrl="https://feeds.megaphone.fm/SGP8517078272"  htmlUrl="https://getsleepy.com" />
<outline text="In the Making" type="rss" xmlUrl="https://feeds.simplecast.com/IWd_z6c8"  htmlUrl="https://www.behance.net/wireframepodcast" />
<outline text="文學嚼一錠Literature" type="rss" xmlUrl="https://feed.firstory.me/rss/user/cl75oj0i300hk01tacthrhmsk"  htmlUrl="https://open.firstory.me/user/cl75oj0i300hk01tacthrhmsk" />
<outline text="大師輕鬆讀之輕鬆聽大師" type="rss" xmlUrl="https://feeds.soundon.fm/podcasts/ab9bc9fe-d1f7-416b-bd60-b4b77be6a49a.xml"  htmlUrl="https://www.master60.com.tw" />
<outline text="靈魂相談室" type="rss" xmlUrl="https://feeds.soundon.fm/podcasts/968c897a-2f28-40fc-9907-d00c833f343d.xml"  htmlUrl="https://www.facebook.com/RitaW19101" />
<outline text="故事FM" type="rss" xmlUrl="https://storyfm.cn/feed/episodes"  htmlUrl="https://storyfm.cn/" />
<outline text="Meditative Story" type="rss" xmlUrl="https://rss.art19.com/meditative-story"  htmlUrl="http://www.meditativestory.com" />
<outline text="StoryCorps" type="rss" xmlUrl="https://feeds.npr.org/510200/podcast.xml"  htmlUrl="https://www.npr.org/podcasts/510200/storycorps" />
<outline text="懷哲的podcast" type="rss" xmlUrl="https://feed.firstory.me/rss/user/cjyqp92m12pzi0743w586b3sm"  htmlUrl="https://open.firstory.me/user/cjyqp92m12pzi0743w586b3sm" />
<outline text="Dear Therapists with Lori Gottlieb and Guy Winch" type="rss" xmlUrl="https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/40d70f44-0da7-469d-be6a-ae390045e52d/7a5e26f6-f408-4130-b280-ae390045e53b/podcast.rss"  htmlUrl="https://www.iheart.com/podcast/1119-dear-therapists-68853191/" />
<outline text="WorkLife with Adam Grant" type="rss" xmlUrl="https://feeds.feedburner.com/worklifewithadamgrant"  htmlUrl="https://www.ted.com/podcasts/worklife" />
<outline text="Hidden Brain" type="rss" xmlUrl="https://feeds.simplecast.com/kwWc0lhf"  htmlUrl="https://www.stitcher.com" />
<outline text="The Stoop Storytelling Series" type="rss" xmlUrl="https://www.omnycontent.com/d/playlist/884f8f20-18c0-4e45-968d-ac17005beefe/4476d439-dd99-4815-9bd4-aee100fd81fc/53582cab-2194-4ab1-9147-aee100fd8221/podcast.rss"  htmlUrl="http://www.stoopstorytelling.com/" />
<outline text="Soft Skills Engineering" type="rss" xmlUrl="https://softskills.audio/feed.xml"  htmlUrl="https://softskills.audio/" />
<outline text="How to Be a Better Human" type="rss" xmlUrl="https://feeds.feedburner.com/howtobeabetterhuman"  htmlUrl="https://play.prx.org/listen?uf=https%3A%2F%2Ffeeds.feedburner.com%2FHowToBeABetterHuman" />
<outline text="You Are Not So Smart" type="rss" xmlUrl="https://feeds.simplecast.com/N5eKDxJI"  htmlUrl="https://www.stitcher.com" />
<outline text="Fixable" type="rss" xmlUrl="https://feeds.feedburner.com/ted_fixable"  htmlUrl="http://audiocollective.ted.com" />
<outline text="文森說書" type="rss" xmlUrl="https://feeds.buzzsprout.com/1096139.rss"  htmlUrl="https://www.youtube.com/channel/UCPgGtH2PxZ9xR0ehzQ27FHw" />
<outline text="This American Life" type="rss" xmlUrl="https://www.thisamericanlife.org/podcast/rss.xml"  htmlUrl="https://www.thisamericanlife.org" />
<outline text="Positive Leadership" type="rss" xmlUrl="https://feeds.buzzsprout.com/1798971.rss"  htmlUrl="https://thepositiveleadershippodcast.buzzsprout.com/" />
<outline text="Climate Rising" type="rss" xmlUrl="https://feeds.megaphone.fm/TPG7476737324"  htmlUrl="https://www.hbs.edu/environment/podcast/Pages/default.aspx" />
<outline text="Psychology Tidbits" type="rss" xmlUrl="https://www.spreaker.com/show/1380473/episodes/feed"  htmlUrl="http://www.thecircleofinsight.com" />
<outline text="Radio Diaries" type="rss" xmlUrl="https://feed.radiodiaries.org/radio-diaries"  htmlUrl="http://www.radiodiaries.org" />
<outline text="Mind The Business: Small Business Success Stories" type="rss" xmlUrl="https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/18b0e863-f0c3-4eac-8d15-afc0015a6924/a80a5778-5738-4e50-b991-afc0015cd172/podcast.rss"  htmlUrl="https://www.iheart.com/podcast/1119-mind-the-business-small-b-110261717/" />
<outline text="Tiny Dinos" type="rss" xmlUrl="https://feeds.megaphone.fm/tinydinos"  htmlUrl="https://hyperobjectindustries.com/podcasts/tiny-dinos" />
<outline text="Grown-Up Stuff: How to Adult" type="rss" xmlUrl="https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/1b36bef5-b515-4e5a-a41c-affa00ea1bed/5791c797-eaca-40d3-bc1b-affa00ead276/podcast.rss"  htmlUrl="https://www.iheart.com/podcast/1119-grown-up-stuff-how-to-adu-114754620/" />
<outline text="瑟谷辣媽愛聊天" type="rss" xmlUrl="https://feed.firstory.me/rss/user/ckjzc1o0twqye08207r5k0uo8"  htmlUrl="https://open.firstory.me/user/ckjzc1o0twqye08207r5k0uo8" />
<outline text="心理不用學" type="rss" xmlUrl="https://feed.firstory.me/rss/user/cl4qw0yp800sh01wagkvkh4vt"  htmlUrl="https://open.firstory.me/user/cl4qw0yp800sh01wagkvkh4vt" />
<outline text="The TED Interview" type="rss" xmlUrl="https://feeds.feedburner.com/TedInterview"  htmlUrl="https://www.ted.com/podcasts/ted-interview" />
<outline text="阿Ken之聲" type="rss" xmlUrl="https://feed.firstory.me/rss/user/clhkit5tj04ed01xo7ppn0r1g"  htmlUrl="https://open.firstory.me/user/akensvioce" />
<outline text="Duolingo French Podcast" type="rss" xmlUrl="https://frpodcast.libsyn.com/rss"  htmlUrl="https://podcast.duolingo.com/french" />
<outline text="The Art of War by Sun Tzu" type="rss" xmlUrl="http://www.loyalbooks.com/book/the-art-of-war-by-sun-tzu/feed"  htmlUrl="http://www.loyalbooks.com/book/the-art-of-war-by-sun-tzu" />
<outline text="Rough Translation" type="rss" xmlUrl="https://feeds.npr.org/510324/podcast.xml"  htmlUrl="https://www.npr.org/podcasts/510324/rough-translation" />
<outline text="Awaken" type="rss" xmlUrl="https://feeds.transistor.fm/awaken"  htmlUrl="https://rubinmuseum.org/landing/awaken" />
<outline text="三十男的書適圈" type="rss" xmlUrl="https://feed.firstory.me/rss/user/ckrgezl9owqwj0854ktaxbvfz"  htmlUrl="https://open.firstory.me/user/timanddan" />
<outline text="What You Will Learn" type="rss" xmlUrl="https://feeds.acast.com/public/shows/91558a12-71f8-4c39-92ee-d7d11318ec4f"  htmlUrl="http://www.whatyouwilllearn.com" />
<outline text="Pondercast" type="rss" xmlUrl="https://pondercast.libsyn.com/playerfm"  htmlUrl="https://www.pondercast.ca" />
<outline text="Ground Level" type="rss" xmlUrl="https://groundlevel.libsyn.com/playerfm"  htmlUrl="https://www.pondercast.ca/ground-level" />
<outline text="百靈果 Book Club" type="rss" xmlUrl="https://feeds.soundon.fm/podcasts/7b249164-aa26-467d-88a2-899fba1b6c91.xml"  htmlUrl="https://www.instagram.com/bailingguo_news" />
<outline text="Dada阿姨說故事" type="rss" xmlUrl="http://www.ximalaya.com/album/8086937.xml"  htmlUrl="https://www.ximalaya.com/album/8086937" />
<outline text="安安老师的心理课" type="rss" xmlUrl="http://rss.lizhi.fm/rss/271126.xml"  htmlUrl="http://www.lizhi.fm" />
'''

# Regular expression to find all xmlUrl attributes
urls = re.findall(r'xmlUrl="([^"]+)"', xml_content)

# Print the results
for url in urls:
    print(url)

# urls = [
#     "https://url1.com",
#     "https://url2.com",
#     # Add more URLs here
# ]
for url in urls:
    # Open a new tab in your browser (assuming the browser is already open)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)

    # Type the URL and press Enter
    pyautogui.write(url)
    pyautogui.press('enter')
    time.sleep(3)  # Wait for the page to load

    # Click the first button (you'll need to know the exact screen position)
    pyautogui.click(x=100, y=200)  # Replace with actual coordinates
    time.sleep(1)

    # Click the second button
    pyautogui.click(x=150, y=250)  # Replace with actual coordinates
    time.sleep(1)

    # Paste the URL in the text box (you'll need to know the screen position)
    pyautogui.click(x=200, y=300)  # Replace with actual coordinates
    pyautogui.write(url)

    # Click the final submit button
    pyautogui.click(x=250, y=350)  # Replace with actual coordinates
    time.sleep(2)

    # Optional: Close the tab (if necessary)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1)
