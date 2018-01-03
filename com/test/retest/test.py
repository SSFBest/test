#-*- coding: utf-8 -*-
'''
Created on 2010-5-27

@author: Administrator
'''
import re

def matchImg():
    str=u'<p style="text-align: center;"><img src="/assets/aa/2014/07/20/coolfg_005_20140720225406_960.jpg" alt="coolfg_005_20140720225406_960.jpg"/></p><p style="text-align: center;"><img src="/assets/aa/2014/07/20/coolfg_005_20140720225406_961.jpg" alt="coolfg_005_20140720225406_961.jpg"/></p>'
    p = re.compile(r'/assets/aa/[^\"]*\.jpg')
    iterator = p.finditer(str)
    for m in iterator:
        print m.group()
        # break
def testre():
	subject='abc style  =  "hbackground=black;"'
	content, number = re.subn(r'style\s*={1}\s*[\'\"]{1}[^\'\"]*[\'\"]{1}', '', subject)
	print content
	print number
def testre12():
    c=u'''<p>
    　　2015年7月31日下午，NVIDIA2015游戏畅想会在上海浦东嘉里酒店召开，包括新浪游戏在内的十五家媒体受邀参加了本次会议。
</p>'''
    # print c.encode('utf-8')
    result,num=re.subn(u'<p>[\s\u3000]+', '<p>', c)
    print result.encode('utf-8')
    print num
def testre3():
    content="""
    <div id="artibody">
<p>　　<strong>【新浪游戏微博报道，敬请关注@新浪游戏】</strong></p>

<p>　　北京时间8月19日，据完美世界(NASDAQ：PWRD)公布的财务报告(截至2014年6月30日的第二季度未经审计的)显示，2014年第二季度完美世界的营业收入达到约9.3亿，创历史最高水平，而在线游戏作为对营业收入贡献最大的部分，增长劲头强劲，约达到8.6亿。</p>

<div class="img_wrapper"><img alt="完美世界Q2财报发布 营收创历史新高" height="332" src="/assets/aa/gm/2014/0819/U10515P115DT20140819094207_pc.jpg" title="完美世界Q2财报发布 营收创历史新高" width="500"></div>

<p>　　财报显示，2014年第二季度完美世界营业收入总额达到928.4百万元人民币(149.6百万美元)，较去年同期(700.1百万元人民币)增长了32.6%。</p>

<p>　　在完美世界本季度营业收入总额的构成中，在线游戏营业收入(包括国内及海外在线游戏营业收入)达到861.1百万元人民币(138.8百万美元)，较去年同期(650.1百万元人民币)增长了32.5%，对总营收的贡献最大。</p>

<div class="img_wrapper"><img alt="完美世界Q2财报发布 营收创历史新高" height="285" src="/assets/aa/gm/2014/0819/U10515P115DT20140819094230_pc.jpg" title="完美世界Q2财报发布 营收创历史新高" width="500"></div>

<p>　　完美世界方面表示，在线游戏营业收入增加，主要受到客户端网络游戏如旗舰产品《笑傲江湖》等的收入贡献增加和《DOTA2》的贡献逐步增长，以及《神魔大陆》和《魔力宝贝》等移动网络游戏的良好表现。</p>

<p>　　此外，本季度完美世界授权收入为48.9百万元人民币(7.9百万美元)，较去年同期的31.5百万元人民币增长了55.2%。授权收入较上季度的增长主要与本季度完美世界在某些海外市场推出的移动游戏有关。</p>

<div class="img_wrapper"><img alt="完美世界Q2财报发布 营收创历史新高" height="294" src="/assets/aa/gm/2014/0819/U10515P115DT20140819094255_pc.jpg" title="完美世界Q2财报发布 营收创历史新高" width="500"></div>

<p>　　在第二季度完美世界营收创新高的同时，营业利润也出现大幅增长，2014年第二季度完美世界的营业利润为128.2百万元人民币(20.7百万美元)，去年同期为72.6百万元人民币。增长率达到76.6%。</p>

<p>　　本季度完美世界的毛利为678.6百万元人民币(109.4百万美元)，去年同期为535.5百万元人民币。归属于完美世界股东的净利润为161.7百万元人民币，比去年同期的80.7百万元人民币增长了100.4%。</p>

<p>　　From：中国新闻网</p><p style="font-size:12px;color:#03005C;"><strong>声明：</strong>新浪网游戏频道登载此文出于传递信息之目的，绝不意味着新浪公司赞同其观点或证实其描述。</p></div>
    """
    m = re.search(r'(/assets/aa.*\.jpg)', content)
    print '0000',m.groups()
    print '11111111111111111111'
    print m.group(0)
    print m.group(1)
    print '11111111111111111111'
    content, number=re.subn(r'(/assets/aa.*)_pc(\.jpg)', r'%s\1_phone\2'%('http://static.youxi16.com'), content)
    # content, number=re.subn(r'(/assets/aa.*\.jpg)', r'%s\1'%('http://static.youxi16.com'), content)
    print content
    print number
def testre2():
    content="""
    <div id="artibody">
<p>　　<strong>【新浪游戏微博报道，敬请关注@新浪游戏】</strong></p>

<p>　　北京时间8月19日，据完美世界(NASDAQ：PWRD)公布的财务报告(截至2014年6月30日的第二季度未经审计的)显示，2014年第二季度完美世界的营业收入达到约9.3亿，创历史最高水平，而在线游戏作为对营业收入贡献最大的部分，增长劲头强劲，约达到8.6亿。</p>

<div class="img_wrapper"><img alt="完美世界Q2财报发布 营收创历史新高" height="332" src="http://i1.sinaimg.cn/gm/2014/0819/U10515P115DT20140819094207.jpg" title="完美世界Q2财报发布 营收创历史新高" width="500"></div>

<p>　　财报显示，2014年第二季度完美世界营业收入总额达到928.4百万元人民币(149.6百万美元)，较去年同期(700.1百万元人民币)增长了32.6%。</p>

<p>　　在完美世界本季度营业收入总额的构成中，在线游戏营业收入(包括国内及海外在线游戏营业收入)达到861.1百万元人民币(138.8百万美元)，较去年同期(650.1百万元人民币)增长了32.5%，对总营收的贡献最大。</p>

<div class="img_wrapper"><img alt="完美世界Q2财报发布 营收创历史新高" height="285" src="http://i1.sinaimg.cn/gm/2014/0819/U10515P115DT20140819094230.jpg" title="完美世界Q2财报发布 营收创历史新高" width="500"></div>

<p>　　完美世界方面表示，在线游戏营业收入增加，主要受到客户端网络游戏如旗舰产品《笑傲江湖》等的收入贡献增加和《DOTA2》的贡献逐步增长，以及《神魔大陆》和《魔力宝贝》等移动网络游戏的良好表现。</p>

<p>　　此外，本季度完美世界授权收入为48.9百万元人民币(7.9百万美元)，较去年同期的31.5百万元人民币增长了55.2%。授权收入较上季度的增长主要与本季度完美世界在某些海外市场推出的移动游戏有关。</p>

<div class="img_wrapper"><img alt="完美世界Q2财报发布 营收创历史新高" height="294" src="http://i0.sinaimg.cn/gm/2014/0819/U10515P115DT20140819094255.jpg" title="完美世界Q2财报发布 营收创历史新高" width="500"></div>

<p>　　在第二季度完美世界营收创新高的同时，营业利润也出现大幅增长，2014年第二季度完美世界的营业利润为128.2百万元人民币(20.7百万美元)，去年同期为72.6百万元人民币。增长率达到76.6%。</p>

<p>　　本季度完美世界的毛利为678.6百万元人民币(109.4百万美元)，去年同期为535.5百万元人民币。归属于完美世界股东的净利润为161.7百万元人民币，比去年同期的80.7百万元人民币增长了100.4%。</p>

<p>　　From：中国新闻网</p><p style="font-size:12px;color:#03005C;"><strong>声明：</strong>新浪网游戏频道登载此文出于传递信息之目的，绝不意味着新浪公司赞同其观点或证实其描述。</p></div>
    """
    content, number=re.subn(r'<p\s+style\s*=\s*"[^"]*"\s*>\s*<strong>.*</strong>.*</p>', '', content)
    print content
    print number

def testre4():
    content="""
    <p>　　4月2日，由触控科技主办的“Cocos 2015开发者大会(春季)”将在北京国家会议中心开幕。本届大会主题为“Power up, game  on.”，将与cocos开发者和与会者分享cocos引擎及工具链产品的最新技术与趋势，cocos开发者生态圈的最新动态。历经了一番抢票热潮之后，大会开幕在即。</p><div class="img_wrapper"><img alt="　　" src="/assets/aa/new/2015/03/31/552613cf7d7702b8a087cf4e0f3dc8b1419e0bac_pc.jpg" title="　　"><span class="img_descr">　　</span></div><p>　　除了分享最新的cocos技术和移动资讯，大会邀请到了各路移动游戏市场知名厂商，与cocos开发者平台一起，为广大开发者营造了一个开放共赢的开发者生态系统。巨头企业包括微软、英特尔、ARM、亚马逊、谷歌、高通;手游周边服务厂商包括畅思广告、Chartboost、Testin、DataEye、WeRec、TalkingData等众多知名厂商都将出现在合作分会场，带来更多有关移动市场、行业前景以及发展趋势的思考。</p><div class="img_wrapper"><img alt=" " src="/assets/aa/new/2015/03/31/7f543a08680967449bc49629801756c275f88183_pc.jpg" title=" "><span class="img_descr"> </span></div><p>　　自cocos引擎诞生之初，触控科技就一直与微软、英特尔、谷歌、亚马逊等众多巨头企业保持着密切的合作关系，这也就解释了为什么作为重磅嘉宾的各大巨头会纷纷现身此次大会。在本次大会上，微软将会发布重磅新闻，开启一个带给开发者惊喜的全球活动--Cocos游戏Windows开发大赛。大赛详情、悬赏奖金等细节将在大会上午由微软Windows应用商店及开发者平台，高级产品市场经理Sonal  Pardeshi亲自揭晓!是不是非常期待呢?此外，微软还将分享Azure微软云服务的相关资讯，助力手游行业茁壮成长。</p><p>　　随着移动互联的社交化渗透，以HTML5游戏为代表的移动轻游戏开始风靡，微信这一国民级App壮大成一个超级HTML5渠道。提升用户体验，把握HTML5这一庞大的市场已经成为不少开发者心中所想。英特尔作为全球最大的CPU制造商，曾在硬件层面为cocos引擎做优化，全面提升cocos游戏的流畅程度，打造更完美的用户体验，此次大会英特尔将发布新的计划--蓄力HTML5游戏的开发，帮助开发者把握HTML5市场，精彩内容不容错过。</p><p>　　谷歌毫无疑问是全球广告领域霸主级的存在，同时也是触控科技长久以来的战略合作伙伴之一。移动市场风云变幻，广告不失为开发者将流量变现的一种便捷途径。但在苹果商店一次次地更改积分排行规则，国内安卓渠道多、杂、乱的环境之下，未来移动广告如何发展?不妨来大会现场听一听谷歌的解决方案。</p><p>　　此外亚马逊AWS也将在合作分会场带来其助力游戏公司取得全球性成功的分享，致力为开发者提供更优质的云服务。畅思广告、Charboost、Testin、DataEye、WeRec、TalkingData等专注移动游戏研发周边产业的知名服务商也将从流量变现、游戏测试、营销数据、精准统计等多个方面，剖析手游研发过程中可能遇到的各样问题，给出快速有效的解决方案。</p><div class="img_wrapper"><img alt=" " src="/assets/aa/new/2015/03/31/e8e020c7d0509fdbed4c0983d11e414c56f7a8a8_pc.jpg" title=" "><span class="img_descr"> </span></div><p>　　当然，纸上得来终觉浅，不如现场看一看。Cocos  2015开发者大会(春季)官网余票已经不多，还没有购票的小伙伴们如果不抓紧时间，就将面临无票可抢的残酷现实!现在就登录赶紧给自己留个座吧!前500名到大会现场签到的与会者更有限量版Cocos玩偶相赠!</p><p>　　另据大会VIP门票摩点众筹活动显示，截至3月27日，大会VIP门票也已达成154.88%超额售出!与cocos引擎两位开创人物--张晓龙与Ricardo  Quesada共进技术大牛午餐会的机会，也即将售罄!VIP门票众筹活动请点击：</p><p>　　2015年4月2日，cocos在北京国家会议中心等你，不见不散!</p>
    """
    print '11111111111111111111'
    m = re.search(r'(/assets/aa/new/\d{4}/\d{2}/\d{2}/[0-9A-Za-z]{40})_pc(\.jpg)', content)
    print '000', m.groups()
    print '111', m.group(0)
    print '2222', m.group(1)
    print  '333',m.group(2)
    print '11111111111111111111'
    content, number=re.subn(r'(/assets/aa/new/\d{4}/\d{2}/\d{2}/[0-9A-Za-z]{40})_pc(\.jpg)', r'%s\1_phone\2'%('http://static.youxi16.com'), content)
    # content, number=re.subn(r'(/assets/aa.*\.jpg)', r'%s\1'%('http://static.youxi16.com'), content)
    print content
    print number

if __name__ == '__main__':
    # matchImg()
    # testre2()
    # testre3()
    # testre4()
    testre12()
    
