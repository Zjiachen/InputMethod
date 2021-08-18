from xpinyin import Pinyin
from PIL import Image,ImageDraw
import math
# 图片对应的像素位置
keyMappings = {"esc":(40,73,5),"~":(40, 118,1),"`":(40,118,1),"1":(93 ,118,1),"2":(146, 118,1),"3":(199, 118,1),"4":(255, 118,1),"5":(308, 118,1),"6":(362, 118,1),"7":(417, 118,1),"8":(470, 118,1),"9":(525, 118,1),"0":(579, 118,1),"!":(93 ,118,1),"@":(146, 118,1),"#":(199, 118,1),"$":(255, 118,1),"%":(308, 118,1),"^":(362, 118,1),"&":(417, 118,1),"*":(470, 118,1),"(":(525, 118,1),")":(579, 118,1),"-":(633, 118,1),"=":(686, 118,1),"_":(633, 118,1),"+":(686, 118,1),"del":(755, 118,2),"tab":(50 ,171,2),"q":(118, 171,1),"w":(172, 171,1),"e":(226, 171,1),"r":(280, 171,1),"t":(334, 171,1),"y":(388, 171,1),"u":(442, 171,1),"i":(496, 171,1),"o":(550, 171,1),"p":(604, 171,1),"[":(658, 171,1),"{":(658, 171,1),"]":(712, 171,1),"}":(712, 171,1),"\\":(766, 171,1),"|":(766, 171,1),"a":(133, 222,1),"s":(187, 222,1),"d":(241, 222,1),"f":(295, 222,1),"g":(349, 222,1),"h":(403, 222,1),"j":(457, 222,1),"k":(511, 222,1),"l":(565, 222,1),":":(619, 222,1),";":(619, 222,1),"'":(673, 222,1),"\"":(673, 222,1),"\n":(752, 222,3),"shift":(76 ,275,4),"z":(160, 275,1),"x":(214, 275,1),"c":(268, 275,1),"v":(322, 275,1),"b":(376, 275,1),"n":(430, 275,1),"m":(484, 275,1),",":(538, 275,1),".":(592, 275,1),"<":(538, 275,1),">":(592, 275,1),"/":(646, 275,1),"?":(646, 275,1),"fn":(39 ,331,7),"ctrl":(92 ,331,7),"opt":(147, 331,7),"cmd":(207, 331,8)," ":(378, 331, 6),"up":(714, 318,5),"left":(660, 343,5),"down":(714, 343,5),"right":(767, 343,5)}
# 将拼音与双字符输入转化
Transfer_Table={
    "ba": "ba",
    "bo": "bo",
    "bi": "be",
    "bu": "bu",
    "bai": "bq",
    "bei": "bw",
    "bao": "br",
    "bie": "bt",
    "ban": "by",
    "ben": "bo",
    "bin": "bp",
    "bang": "bs",
    "beng": "bd",
    "bing": "bf",
    "bian": "bg",
    "biao": "bh",

    "pa": "pa",
    "po": "po",
    "pi": "pi",
    "pu": "pu",
    "pai": "pj",
    "pei": "pk",
    "pao": "pl",
    "pou": "pz",
    "pie": "px",
    "pan": "pc",
    "pen": "pv",
    "pin": "pb",
    "pang": "pn",
    "peng": "pm",
    "ping": "pq",
    "pian": "pw",
    "piao": "pe",

    "ma": "ma",
    "mo": "mo",
    "me": "me",
    "mi": "mi",
    "mu": "mu",
    "mai": "mr",
    "mei": "mt",
    "mao": "my",
    "mou": "mp",
    "miu": "ms",
    "mie": "md",
    "man": "mf",
    "men": "mg",
    "min": "mh",
    "mang": "mj",
    "meng": "mk",
    "ming": "ml",
    "mian": "mz",
    "miao": "mx",

    "fa": "fa",
    "fo": "fo",
    "fu": "fu",
    "fei": "fc",
    "fou": "fv",
    "fan": "fb",
    "fen": "fn",
    "fang": "fm",
    "feng": "fq",

    "da": "da",
    "de": "de",
    "di": "di",
    "du": "du",
    "dai": "dw",
    "dei": "dr",
    "dui": "dt",
    "dao": "dy",
    "dou": "do",
    "diu": "dp",
    "die": "ds",
    "dan": "dd",
    "den": "df",
    "dun": "dg",
    "dang": "dh",
    "ding": "dj",
    "dong": "dk",
    "dia": "dl",
    "dian": "dz",
    "diao": "dx",
    "duan": "dc",
    "duo": "dv",

    "ta": "ta",
    "te": "te",
    "ti": "ti",
    "tu": "tu",
    "tai": "tb",
    "tui": "tn",
    "tao": "tm",
    "tou": "tq",
    "tie": "tw",
    "tan": "tr",
    "tun": "ty",
    "tang": "to",
    "teng": "tp",
    "ting": "ts",
    "tong": "td",
    "tian": "tf",
    "tuan": "tg",
    "tuo": "th",

    "na": "na",
    "ne": "ne",
    "ni": "ni",
    "nu": "nu",
    "nv": "nv",
    "nai": "nj",
    "nei": "nk",
    "nao": "nl",
    "nou": "nz",
    "niu": "nx",
    "nie": "nc",
    "nue": "nb",
    "nan": "nm",
    "nen": "nq",
    "nin": "nw",
    "nang": "nr",
    "neng": "nt",
    "ning": "ny",
    "nong": "no",
    "nian": "np",
    "niang": "ns",
    "niao": "nd",
    "nuan": "nf",
    "nuo": "ng",

    "la": "la",
    "lo": "lo",
    "le": "le",
    "li": "li",
    "lu": "lu",
    "lv": "lv",
    "lai": "lh",
    "lei": "lj",
    "lao": "lk",
    "lou": "ll",
    "liu": "lz",
    "lie": "lx",
    "lue": "lc",
    "lan": "lv",
    "lin": "lb",
    "lun": "ln",
    "lang": "lm",
    "leng": "lq",
    "ling": "lw",
    "long": "lr",
    "lia": "lt",
    "lian": "ly",
    "liang": "lp",
    "liao": "ls",
    "luan": "ld",
    "luo": "lf",

    "ga": "ga",
    "ge": "ge",
    "gu": "gu",
    "gai": "gg",
    "gei": "gh",
    "gui": "gj",
    "gao": "gk",
    "gou": "gl",
    "gan": "gz",
    "gen": "gx",
    "gun": "gc",
    "gang": "gv",
    "geng": "gb",
    "gong": "gn",
    "gua": "gm",
    "guai": "gq",
    "guan": "gw",
    "guang": "gr",
    "guo": "gt",

    "ka": "ka",
    "ke": "ke",
    "ku": "ku",
    "kai": "ky",
    "kei": "ki",
    "kui": "ko",
    "kao": "kp",
    "kou": "ks",
    "kan": "kd",
    "ken": "kf",
    "kun": "kg",
    "kang": "kh",
    "keng": "kj",
    "kong": "kk",
    "kua": "kl",
    "kuai": "kz",
    "kuan": "kx",
    "kuang": "kc",
    "kuo": "kv",

    "ha": "ha",
    "he": "he",
    "hu": "hu",
    "hai": "hb",
    "hei": "hn",
    "hui": "hm",
    "hao": "hq",
    "hou": "hw",
    "han": "hr",
    "hen": "ht",
    "hun": "hy",
    "hang": "hi",
    "heng": "ho",
    "hong": "hp",
    "hua": "hs",
    "huai": "hd",
    "huan": "hf",
    "huang": "hg",
    "huo": "hh",

    "ji": "ji",
    "ju": "ju",
    "jiu": "jj",
    "jie": "jk",
    "jue": "jl",
    "jin": "jz",
    "jun": "jx",
    "jing": "jc",
    "jia": "jv",
    "jian": "jb",
    "jiang": "jn",
    "jiao": "jm",
    "jiong": "jq",
    "juan": "jw",

    "qi": "qi",
    "qu": "qu",
    "qiu": "qe",
    "qie": "qr",
    "que": "qt",
    "qin": "qy",
    "qun": "qo",
    "qing": "qp",
    "qia": "qa",
    "qian": "qs",
    "qiang": "qd",
    "qiao": "qf",
    "qiong": "qg",
    "quan": "qh",

    "xi": "xi",
    "xu": "xu",
    "xiu": "xj",
    "xie": "xk",
    "xue": "xl",
    "xin": "xz",
    "xun": "xx",
    "xing": "xc",
    "xia": "xv",
    "xian": "xb",
    "xiang": "xn",
    "xiao": "xm",
    "xiong": "xq",
    "xuan": "xw",

    "zha": "va",
    "zhe": "ve",
    "zhi": "vi",
    "zhu": "vu",
    #
    "zhai": "ve",
    "zhei": "vr",
    #
    "zhui": "vt",
    "zhao": "vy",
    "zhou": "vo",
    "zhan": "vp",
    "zhen": "vs",
    "zhun": "vd",
    "zhang": "vf",
    "zheng": "vg",
    "zhong": "vh",
    "zhua": "vj",
    "zhuai": "vk",
    "zhuan": "vl",
    "zhuang": "vz",
    "zhuo": "vx",

    "cha": "ua",
    "che": "ue",
    "chi": "ui",
    "chu": "uu",
    "chai": "uc",
    "chui": "uv",
    "chao": "ub",
    "chou": "un",
    "chan": "um",
    "chen": "uq",
    "chun": "uw",
    "chang": "ur",
    "cheng": "ut",
    "chong": "uy",
    "chua": "uo",
    "chuai": "up",
    "chuan": "us",
    "chuang": "ud",
    "chuo": "uf",

    "sha": "ia",
    "she": "ie",
    "shi": "ii",
    "shu": "iu",
    "shai": "ig",
    "shei": "ih",
    "shui": "ij",
    "shao": "ik",
    "shou": "il",
    "shan": "iz",
    "shen": "ix",
    "shun": "ic",
    "shang": "iv",
    "sheng": "ib",
    "shua": "in",
    "shuai": "im",
    "shuan": "iq",
    "shuang": "iw",
    "shuo": "it",


    "re": "re",
    "ri": "ri",
    "ru": "ru",
    "rui": "ry",
    "rao": "ro",
    "rou": "rp",
    "ran": "ra",
    "ren": "rs",
    "run": "rd",
    "rang": "rf",
    "reng": "rg",
    "rong": "rh",
    "rua": "rj",
    "ruan": "rk",
    "ruo": "rl",

    "za": "za",
    "ze": "ze",
    "zi": "zi",
    "zu": "zu",
    "zai": "zz",
    "zei": "zx",
    "zui": "zc",
    "zao": "zv",
    "zou": "zb",
    "zan": "zn",
    "zen": "zm",
    "zun": "zq",
    "zang": "zw",
    "zeng": "zr",
    "zong": "zt",
    "zuan": "zy",
    "zuo": "zo",

    "ca": "ca",
    "ce": "ce",
    "ci": "ci",
    "cu": "cu",
    "cai": "cp",
    "cui": "cs",
    "cao": "cd",
    "cou": "cf",
    "can": "cg",
    "cen": "ch",
    "cun": "cj",
    "cang": "ck",
    "ceng": "cl",
    "cong": "cz",
    "cuan": "cx",
    "cuo": "cc",

    "sa": "sa",
    "se": "se",
    "si": "si",
    "su": "su",
    "sai": "sv",
    "sui": "sb",
    "sao": "sn",
    "sou": "sm",
    "san": "sq",
    "sen": "sw",
    "sun": "sr",
    "sang": "st",
    "seng": "sy",
    "song": "so",
    "suan": "sp",
    "suo": "ss",

    "ya": "ya",
    "yo": "yo",
    "ye": "ye",
    "yi": "yi",
    "yu": "yu",
    "yao": "yd",
    "you": "yf",
    "yue": "yg",
    "yan": "yh",
    "yin": "yj",
    "yun": "yk",
    "yang": "yl",
    "ying": "yz",
    "yong": "yx",
    "yuan": "yc",

    "wa": "wa",
    "wo": "wo",
    "wu": "wu",
    "wai": "wv",
    "wei": "wb",
    "wan": "wn",
    "wen": "wm",
    "wang": "wq",
    "weng": "ww",

    "a": "a",
    "ao": "ao",
    "ai": "ao",
    "an": "an",
    "ang": "am",

    "ou": "ou",

    "ei": "ei",
    "e": "e",
    "er": "er",
    "en": "en"
}


class ArticleAnalysis:
    def __init__(self, path):
        self.PATH = path
        self.sum = 0
        self.total_words=0
        self.average = 0
        self.varience=0
        self.hot_list = []
        self.word_list=[]
        self.article = ''
        self.effective = 0.0
        self.count_dict = {
            "a":0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
            "m": 0,
            "n": 0,
            "o": 0,
            "p": 0,
            "q": 0,
            "r": 0,
            "s": 0,
            "t": 0,
            "u": 0,
            "v": 0,
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0
        }

        with open(self.PATH,'r', encoding='utf-8') as f:
            self.article=f.read()
        # 将txt文章转换为拼音字符串
        p = Pinyin()
        self.result = p.get_pinyin(self.article)

    # 统计使用全拼输入法每个按键使用的次数以及总次数，并计算每个字母的平均出现次数
    def quanpin_static(self):
        # 统计每个按键的使用次数以及总次数

        str="".join(self.word_list)
        self.sum=len(str)
        # 平均使用次数
        self.average = self.sum/26

        # 取超过平均按键次数的按键为热区按键
        for i in self.count_dict:
            if self.count_dict[i]>self.average:
                self.hot_list.append(i)

    # 展示键盘上热力图
    def display(self):
        # 打开图片
        img = Image.open("keyboard.png")
        draw = ImageDraw.Draw(img)
        # 参数：位置、文本、填充、字体
        for i in self.count_dict:
            avaerge: float = self.count_dict[i]/self.sum
            draw.text(xy=(keyMappings[i][0], keyMappings[i][1]),
                      text=str(self.count_dict[i]),
                      fill=(int(avaerge*3000), 0, 0))
        img.show()

    # 分析输入效率以及按键使用均衡性
    # 假设输入效率与按键次数与输入文字数的比值相关，按键使用均衡性与分布的方差，标准差有关
    # 以输入文字数和按键次数的比值，作为输入效率的量化标准, 以标准差作为按键使用的均衡性，标准差差越大均衡性越差
    def anlysis(self):
        print("全拼输入下的按键总数为",self.sum)
        self.effective=self.total_words/self.sum
        print("全拼输入下输入效率值为:",self.effective)
        # 计算方差
        temp = 0
        for i in self.count_dict:
            temp += (self.count_dict[i]-self.average)*(self.count_dict[i]-self.average)
        self.varience=math.sqrt(temp/26)
        print("全拼输入下标准差大小为:",self.varience)
        pass

    # 根据统计结果，可以采用类似双拼输入法的方法 使用两个字符来进行汉字编码,首先输入声母，再根据符合条件的韵母与不同字符产生映射
    def count(self):
        # 将每个字拼音转化为列表形式,并计算总的字数
        buffer=""
        for i in self.result:
            if i.isalpha():
                buffer += i
            elif len(buffer)!=0:
                self.word_list.append(buffer)
                buffer = ""
        self.total_words=len(self.word_list)
        print("文字总数为:",self.total_words)
        pass

    # 将拼音列表对应转化表转化为字符串
    def change(self):
        # 得到转化后的编码字符串
        transtr = ""
        change_sum = 0
        for i in self.word_list:
            if i in Transfer_Table:
                transtr += Transfer_Table[i]
            #  特殊音节暂时用//代替
            else:
                transtr += "//"
        print("转化后的按键总数为", len(transtr))

#                 清空全拼输入的记录
        for i in self.count_dict:
            self.count_dict[i] = 0

#         重新统计新的结果
        for i in transtr:
            if i in self.count_dict:
                self.count_dict[i] += 1
                change_sum += 1
        change_average = change_sum/26
        temp = 0
        for i in self.count_dict:
            temp += (self.count_dict[i] - change_average) * (self.count_dict[i] - change_average)

        varience = math.sqrt(temp / 26)
        effective = self.total_words / change_sum
        print("修改后输入法的效率值为", effective)
        print("修改后输入法的标准差为", varience)


a = ArticleAnalysis('article.txt')
a.count()
a.quanpin_static()
a.display()
a.anlysis()
a.change()
