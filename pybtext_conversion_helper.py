# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 16:37:59 2021

@author: matheus.sartor
"""

import sys

def convert(text: str):
    new_text = str(text).replace(r"{\'{a}}",r"á")\
    .replace(r"{\'{c}}",r"ć")\
    .replace(r"{\'{e}}",r"é")\
    .replace(r"{\'{g}}",r"ǵ")\
    .replace(r"{\'{i}}",r"í")\
    .replace(r"{\'{n}}",r"ń")\
    .replace(r"{\'{o}}",r"ó")\
    .replace(r"{\'{r}}",r"ŕ")\
    .replace(r"{\'{s}}",r"ś")\
    .replace(r"{\'{u}}",r"ú")\
    .replace(r"{\'{w}}",r"ẃ")\
    .replace(r"{\'{y}}",r"ý")\
    .replace(r"{\'{z}}",r"ź")\
    .replace(r"{\'{\a}}",r"á")\
    .replace(r"{\'{\c}}",r"ć")\
    .replace(r"{\'{\e}}",r"é")\
    .replace(r"{\'{\g}}",r"ǵ")\
    .replace(r"{\'{\i}}",r"í")\
    .replace(r"{\'{\n}}",r"ń")\
    .replace(r"{\'{\o}}",r"ó")\
    .replace(r"{\'{\r}}",r"ŕ")\
    .replace(r"{\'{\s}}",r"ś")\
    .replace(r"{\'{\u}}",r"ú")\
    .replace(r"{\'{\w}}",r"ẃ")\
    .replace(r"{\'{\y}}",r"ý")\
    .replace(r"{\'{\z}}",r"ź")\
    .replace(r"{\' a}",r"á")\
    .replace(r"{\' c}",r"ć")\
    .replace(r"{\' e}",r"é")\
    .replace(r"{\' g}",r"ǵ")\
    .replace(r"{\' i}",r"í")\
    .replace(r"{\' n}",r"ń")\
    .replace(r"{\' o}",r"ó")\
    .replace(r"{\' r}",r"ŕ")\
    .replace(r"{\' s}",r"ś")\
    .replace(r"{\' u}",r"ú")\
    .replace(r"{\' w}",r"ẃ")\
    .replace(r"{\' y}",r"ý")\
    .replace(r"{\' z}",r"ź")\
    .replace(r"{\'a}",r"á")\
    .replace(r"{\'c}",r"ć")\
    .replace(r"{\'e}",r"é")\
    .replace(r"{\'g}",r"ǵ")\
    .replace(r"{\'i}",r"í")\
    .replace(r"{\'n}",r"ń")\
    .replace(r"{\'o}",r"ó")\
    .replace(r"{\'r}",r"ŕ")\
    .replace(r"{\'s}",r"ś")\
    .replace(r"{\'u}",r"ú")\
    .replace(r"{\'w}",r"ẃ")\
    .replace(r"{\'y}",r"ý")\
    .replace(r"{\'z}",r"ź")\
    .replace(r"{\'{A}}",r"Á")\
    .replace(r"{\'{C}}",r"Ć")\
    .replace(r"{\'{E}}",r"É")\
    .replace(r"{\'{G}}",r"Ǵ")\
    .replace(r"{\'{I}}",r"Í")\
    .replace(r"{\'{N}}",r"Ń")\
    .replace(r"{\'{O}}",r"Ó")\
    .replace(r"{\'{R}}",r"Ŕ")\
    .replace(r"{\'{S}}",r"Ś")\
    .replace(r"{\'{U}}",r"Ú")\
    .replace(r"{\'{W}}",r"Ẃ")\
    .replace(r"{\'{Y}}",r"Ý")\
    .replace(r"{\'{Z}}",r"Ź")\
    .replace(r"{\'{\a}}",r"Á")\
    .replace(r"{\'{\c}}",r"Ć")\
    .replace(r"{\'{\e}}",r"É")\
    .replace(r"{\'{\G}}",r"Ǵ")\
    .replace(r"{\'{\I}}",r"Í")\
    .replace(r"{\'{\n}}",r"Ń")\
    .replace(r"{\'{\O}}",r"Ó")\
    .replace(r"{\'{\r}}",r"Ŕ")\
    .replace(r"{\'{\S}}",r"Ś")\
    .replace(r"{\'{\U}}",r"Ú")\
    .replace(r"{\'{\W}}",r"Ẃ")\
    .replace(r"{\'{\Y}}",r"Ý")\
    .replace(r"{\'{\Z}}",r"Ź")\
    .replace(r"{\' A}",r"Á")\
    .replace(r"{\' C}",r"Ć")\
    .replace(r"{\' E}",r"É")\
    .replace(r"{\' G}",r"Ǵ")\
    .replace(r"{\' I}",r"Í")\
    .replace(r"{\' N}",r"Ń")\
    .replace(r"{\' O}",r"Ó")\
    .replace(r"{\' R}",r"Ŕ")\
    .replace(r"{\' S}",r"Ś")\
    .replace(r"{\' U}",r"Ú")\
    .replace(r"{\' W}",r"Ẃ")\
    .replace(r"{\' Y}",r"Ý")\
    .replace(r"{\' Z}",r"Ź")\
    .replace(r"{\'A}",r"Á")\
    .replace(r"{\'C}",r"Ć")\
    .replace(r"{\'E}",r"É")\
    .replace(r"{\'G}",r"Ǵ")\
    .replace(r"{\'I}",r"Í")\
    .replace(r"{\'N}",r"Ń")\
    .replace(r"{\'O}",r"Ó")\
    .replace(r"{\'R}",r"Ŕ")\
    .replace(r"{\'S}",r"Ś")\
    .replace(r"{\'U}",r"Ú")\
    .replace(r"{\'W}",r"Ẃ")\
    .replace(r"{\'Y}",r"Ý")\
    .replace(r"{\'Z}",r"Ź")\
    .replace(r"\'{a}",r"á")\
    .replace(r"\'{c}",r"ć")\
    .replace(r"\'{e}",r"é")\
    .replace(r"\'{g}",r"ǵ")\
    .replace(r"\'{i}",r"í")\
    .replace(r"\'{n}",r"ń")\
    .replace(r"\'{o}",r"ó")\
    .replace(r"\'{r}",r"ŕ")\
    .replace(r"\'{s}",r"ś")\
    .replace(r"\'{u}",r"ú")\
    .replace(r"\'{w}",r"ẃ")\
    .replace(r"\'{y}",r"ý")\
    .replace(r"\'{z}",r"ź")\
    .replace(r"\'a",r"á")\
    .replace(r"\'c",r"ć")\
    .replace(r"\'e",r"é")\
    .replace(r"\'g",r"ǵ")\
    .replace(r"\'i",r"í")\
    .replace(r"\'n",r"ń")\
    .replace(r"\'o",r"ó")\
    .replace(r"\'r",r"ŕ")\
    .replace(r"\'s",r"ś")\
    .replace(r"\'u",r"ú")\
    .replace(r"\'w",r"ẃ")\
    .replace(r"\'y",r"ý")\
    .replace(r"\'z",r"ź")\
    .replace(r"\'{\a}",r"á")\
    .replace(r"\'{\c}",r"ć")\
    .replace(r"\'{\e}",r"é")\
    .replace(r"\'{\g}",r"ǵ")\
    .replace(r"\'{\i}",r"í")\
    .replace(r"\'{\n}",r"ń")\
    .replace(r"\'{\o}",r"ó")\
    .replace(r"\'{\r}",r"ŕ")\
    .replace(r"\'{\s}",r"ś")\
    .replace(r"\'{\u}",r"ú")\
    .replace(r"\'{\w}",r"ẃ")\
    .replace(r"\'{\y}",r"ý")\
    .replace(r"\'{\z}",r"ź")\
    .replace(r"\'{A}",r"Á")\
    .replace(r"\'{C}",r"Ć")\
    .replace(r"\'{E}",r"É")\
    .replace(r"\'{G}",r"Ǵ")\
    .replace(r"\'{I}",r"Í")\
    .replace(r"\'{N}",r"Ń")\
    .replace(r"\'{O}",r"Ó")\
    .replace(r"\'{R}",r"Ŕ")\
    .replace(r"\'{S}",r"Ś")\
    .replace(r"\'{U}",r"Ú")\
    .replace(r"\'{W}",r"Ẃ")\
    .replace(r"\'{Y}",r"Ý")\
    .replace(r"\'{Z}",r"Ź")\
    .replace(r"\'A",r"Á")\
    .replace(r"\'C",r"Ć")\
    .replace(r"\'E",r"É")\
    .replace(r"\'G",r"Ǵ")\
    .replace(r"\'I",r"Í")\
    .replace(r"\'N",r"Ń")\
    .replace(r"\'O",r"Ó")\
    .replace(r"\'R",r"Ŕ")\
    .replace(r"\'S",r"Ś")\
    .replace(r"\'U",r"Ú")\
    .replace(r"\'W",r"Ẃ")\
    .replace(r"\'Y",r"Ý")\
    .replace(r"\'Z",r"Ź")\
    .replace(r"\'{\a}",r"Á")\
    .replace(r"\'{\c}",r"Ć")\
    .replace(r"\'{\e}",r"É")\
    .replace(r"\'{\G}",r"Ǵ")\
    .replace(r"\'{\I}",r"Í")\
    .replace(r"\'{\n}",r"Ń")\
    .replace(r"\'{\O}",r"Ó")\
    .replace(r"\'{\r}",r"Ŕ")\
    .replace(r"\'{\S}",r"Ś")\
    .replace(r"\'{\U}",r"Ú")\
    .replace(r"\'{\W}",r"Ẃ")\
    .replace(r"\'{\Y}",r"Ý")\
    .replace(r"\'{\Z}",r"Ź")\
    .replace(r'{\`{a}}',r"à")\
    .replace(r'{\`{e}}',r"è")\
    .replace(r'{\`{i}}',r"ì")\
    .replace(r'{\`{o}}',r"ò")\
    .replace(r'{\`{u}}',r"ù")\
    .replace(r'{\`{\a}}',r"à")\
    .replace(r'{\`{\e}}',r"è")\
    .replace(r'{\`{\i}}',r"ì")\
    .replace(r'{\`{\o}}',r"ò")\
    .replace(r'{\`{\u}}',r"ù")\
    .replace(r'{\` a}',r"à")\
    .replace(r'{\` e}',r"è")\
    .replace(r'{\` i}',r"ì")\
    .replace(r'{\` o}',r"ò")\
    .replace(r'{\` u}',r"ù")\
    .replace(r'{\`a}',r"à")\
    .replace(r'{\`e}',r"è")\
    .replace(r'{\`i}',r"ì")\
    .replace(r'{\`o}',r"ò")\
    .replace(r'{\`u}',r"ù")\
    .replace(r'{\`{A}}',r"À")\
    .replace(r'{\`{E}}',r"È")\
    .replace(r'{\`{I}}',r"Ì")\
    .replace(r'{\`{O}}',r"Ò")\
    .replace(r'{\`{U}}',r"Ù")\
    .replace(r'{\`{\a}}',r"À")\
    .replace(r'{\`{\e}}',r"È")\
    .replace(r'{\`{\I}}',r"Ì")\
    .replace(r'{\`{\O}}',r"Ò")\
    .replace(r'{\`{\U}}',r"Ù")\
    .replace(r'{\` A}',r"À")\
    .replace(r'{\` E}',r"È")\
    .replace(r'{\` I}',r"Ì")\
    .replace(r'{\` O}',r"Ò")\
    .replace(r'{\` U}',r"Ù")\
    .replace(r'{\`A}',r"À")\
    .replace(r'{\`E}',r"È")\
    .replace(r'{\`I}',r"Ì")\
    .replace(r'{\`O}',r"Ò")\
    .replace(r'{\`U}',r"Ù")\
    .replace(r'\`{a}',r"à")\
    .replace(r'\`{e}',r"è")\
    .replace(r'\`{i}',r"ì")\
    .replace(r'\`{o}',r"ò")\
    .replace(r'\`{u}',r"ù")\
    .replace(r'\`a',r"à")\
    .replace(r'\`e',r"è")\
    .replace(r'\`i',r"ì")\
    .replace(r'\`o',r"ò")\
    .replace(r'\`u',r"ù")\
    .replace(r'\`{\a}',r"à")\
    .replace(r'\`{\e}',r"è")\
    .replace(r'\`{\i}',r"ì")\
    .replace(r'\`{\o}',r"ò")\
    .replace(r'\`{\u}',r"ù")\
    .replace(r'\`{A}',r"À")\
    .replace(r'\`{E}',r"È")\
    .replace(r'\`{I}',r"Ì")\
    .replace(r'\`{O}',r"Ò")\
    .replace(r'\`{U}',r"Ù")\
    .replace(r'\`A',r"À")\
    .replace(r'\`E',r"È")\
    .replace(r'\`I',r"Ì")\
    .replace(r'\`O',r"Ò")\
    .replace(r'\`U',r"Ù")\
    .replace(r'\`{\a}',r"À")\
    .replace(r'\`{\e}',r"È")\
    .replace(r'\`{\I}',r"Ì")\
    .replace(r'\`{\O}',r"Ò")\
    .replace(r'\`{\U}',r"Ù")\
    .replace(r'{\^{a}}',r"â")\
    .replace(r'{\^{c}}',r"ĉ")\
    .replace(r'{\^{e}}',r"ê")\
    .replace(r'{\^{g}}',r"ĝ")\
    .replace(r'{\^{i}}',r"î")\
    .replace(r'{\^{j}}',r"ĵ")\
    .replace(r'{\^{o}}',r"ô")\
    .replace(r'{\^{s}}',r"ŝ")\
    .replace(r'{\^{u}}',r"û")\
    .replace(r'{\^{\a}}',r"â")\
    .replace(r'{\^{\c}}',r"ĉ")\
    .replace(r'{\^{\e}}',r"ê")\
    .replace(r'{\^{\g}}',r"ĝ")\
    .replace(r'{\^{\i}}',r"î")\
    .replace(r'{\^{\j}}',r"ĵ")\
    .replace(r'{\^{\o}}',r"ô")\
    .replace(r'{\^{\s}}',r"ŝ")\
    .replace(r'{\^{\u}}',r"û")\
    .replace(r'{\^ a}',r"â")\
    .replace(r'{\^ c}',r"ĉ")\
    .replace(r'{\^ e}',r"ê")\
    .replace(r'{\^ g}',r"ĝ")\
    .replace(r'{\^ i}',r"î")\
    .replace(r'{\^ j}',r"ĵ")\
    .replace(r'{\^ o}',r"ô")\
    .replace(r'{\^ s}',r"ŝ")\
    .replace(r'{\^ u}',r"û")\
    .replace(r'{\^a}',r"â")\
    .replace(r'{\^c}',r"ĉ")\
    .replace(r'{\^e}',r"ê")\
    .replace(r'{\^g}',r"ĝ")\
    .replace(r'{\^i}',r"î")\
    .replace(r'{\^j}',r"ĵ")\
    .replace(r'{\^o}',r"ô")\
    .replace(r'{\^s}',r"ŝ")\
    .replace(r'{\^u}',r"û")\
    .replace(r'{\^{A}}',r"Â")\
    .replace(r'{\^{C}}',r"Ĉ")\
    .replace(r'{\^{E}}',r"Ê")\
    .replace(r'{\^{G}}',r"Ĝ")\
    .replace(r'{\^{I}}',r"Î")\
    .replace(r'{\^{J}}',r"Ĵ")\
    .replace(r'{\^{O}}',r"Ô")\
    .replace(r'{\^{S}}',r"Ŝ")\
    .replace(r'{\^{U}}',r"Û")\
    .replace(r'{\^{\a}}',r"Â")\
    .replace(r'{\^{\c}}',r"Ĉ")\
    .replace(r'{\^{\e}}',r"Ê")\
    .replace(r'{\^{\G}}',r"Ĝ")\
    .replace(r'{\^{\I}}',r"Î")\
    .replace(r'{\^{\J}}',r"Ĵ")\
    .replace(r'{\^{\O}}',r"Ô")\
    .replace(r'{\^{\S}}',r"Ŝ")\
    .replace(r'{\^{\U}}',r"Û")\
    .replace(r'{\^ A}',r"Â")\
    .replace(r'{\^ C}',r"Ĉ")\
    .replace(r'{\^ E}',r"Ê")\
    .replace(r'{\^ G}',r"Ĝ")\
    .replace(r'{\^ I}',r"Î")\
    .replace(r'{\^ J}',r"Ĵ")\
    .replace(r'{\^ O}',r"Ô")\
    .replace(r'{\^ S}',r"Ŝ")\
    .replace(r'{\^ U}',r"Û")\
    .replace(r'{\^A}',r"Â")\
    .replace(r'{\^C}',r"Ĉ")\
    .replace(r'{\^E}',r"Ê")\
    .replace(r'{\^G}',r"Ĝ")\
    .replace(r'{\^I}',r"Î")\
    .replace(r'{\^J}',r"Ĵ")\
    .replace(r'{\^O}',r"Ô")\
    .replace(r'{\^S}',r"Ŝ")\
    .replace(r'{\^U}',r"Û")\
    .replace(r'\^{a}',r"â")\
    .replace(r'\^{c}',r"ĉ")\
    .replace(r'\^{e}',r"ê")\
    .replace(r'\^{g}',r"ĝ")\
    .replace(r'\^{i}',r"î")\
    .replace(r'\^{j}',r"ĵ")\
    .replace(r'\^{o}',r"ô")\
    .replace(r'\^{s}',r"ŝ")\
    .replace(r'\^{u}',r"û")\
    .replace(r'\^a',r"â")\
    .replace(r'\^c',r"ĉ")\
    .replace(r'\^e',r"ê")\
    .replace(r'\^g',r"ĝ")\
    .replace(r'\^i',r"î")\
    .replace(r'\^j',r"ĵ")\
    .replace(r'\^o',r"ô")\
    .replace(r'\^s',r"ŝ")\
    .replace(r'\^u',r"û")\
    .replace(r'\^{\a}',r"â")\
    .replace(r'\^{\c}',r"ĉ")\
    .replace(r'\^{\e}',r"ê")\
    .replace(r'\^{\g}',r"ĝ")\
    .replace(r'\^{\i}',r"î")\
    .replace(r'\^{\j}',r"ĵ")\
    .replace(r'\^{\o}',r"ô")\
    .replace(r'\^{\s}',r"ŝ")\
    .replace(r'\^{\u}',r"û")\
    .replace(r'\^{A}',r"Â")\
    .replace(r'\^{C}',r"Ĉ")\
    .replace(r'\^{E}',r"Ê")\
    .replace(r'\^{G}',r"Ĝ")\
    .replace(r'\^{I}',r"Î")\
    .replace(r'\^{J}',r"Ĵ")\
    .replace(r'\^{O}',r"Ô")\
    .replace(r'\^{S}',r"Ŝ")\
    .replace(r'\^{U}',r"Û")\
    .replace(r'\^A',r"Â")\
    .replace(r'\^C',r"Ĉ")\
    .replace(r'\^E',r"Ê")\
    .replace(r'\^G',r"Ĝ")\
    .replace(r'\^I',r"Î")\
    .replace(r'\^J',r"Ĵ")\
    .replace(r'\^O',r"Ô")\
    .replace(r'\^S',r"Ŝ")\
    .replace(r'\^U',r"Û")\
    .replace(r'\^{\a}',r"Â")\
    .replace(r'\^{\c}',r"Ĉ")\
    .replace(r'\^{\e}',r"Ê")\
    .replace(r'\^{\G}',r"Ĝ")\
    .replace(r'\^{\I}',r"Î")\
    .replace(r'\^{\J}',r"Ĵ")\
    .replace(r'\^{\O}',r"Ô")\
    .replace(r'\^{\S}',r"Ŝ")\
    .replace(r'\^{\U}',r"Û")\
    .replace(r'{\"{a}}',r"ä")\
    .replace(r'{\"{e}}',r"ë")\
    .replace(r'{\"{i}}',r"ï")\
    .replace(r'{\"{o}}',r"ö")\
    .replace(r'{\"{u}}',r"ü")\
    .replace(r'{\"{\a}}',r"ä")\
    .replace(r'{\"{\e}}',r"ë")\
    .replace(r'{\"{\i}}',r"ï")\
    .replace(r'{\"{\o}}',r"ö")\
    .replace(r'{\"{\u}}',r"ü")\
    .replace(r'{\" a}',r"ä")\
    .replace(r'{\" e}',r"ë")\
    .replace(r'{\" i}',r"ï")\
    .replace(r'{\" o}',r"ö")\
    .replace(r'{\" u}',r"ü")\
    .replace(r'{\"a}',r"ä")\
    .replace(r'{\"e}',r"ë")\
    .replace(r'{\"i}',r"ï")\
    .replace(r'{\"o}',r"ö")\
    .replace(r'{\"u}',r"ü")\
    .replace(r'{\"{A}}',r"Ä")\
    .replace(r'{\"{E}}',r"Ë")\
    .replace(r'{\"{I}}',r"Ï")\
    .replace(r'{\"{O}}',r"Ö")\
    .replace(r'{\"{U}}',r"Ü")\
    .replace(r'{\"{\a}}',r"Ä")\
    .replace(r'{\"{\e}}',r"Ë")\
    .replace(r'{\"{\I}}',r"Ï")\
    .replace(r'{\"{\O}}',r"Ö")\
    .replace(r'{\"{\U}}',r"Ü")\
    .replace(r'{\" A}',r"Ä")\
    .replace(r'{\" E}',r"Ë")\
    .replace(r'{\" I}',r"Ï")\
    .replace(r'{\" O}',r"Ö")\
    .replace(r'{\" U}',r"Ü")\
    .replace(r'{\"A}',r"Ä")\
    .replace(r'{\"E}',r"Ë")\
    .replace(r'{\"I}',r"Ï")\
    .replace(r'{\"O}',r"Ö")\
    .replace(r'{\"U}',r"Ü")\
    .replace(r'\"{a}',r"ä")\
    .replace(r'\"{e}',r"ë")\
    .replace(r'\"{i}',r"ï")\
    .replace(r'\"{o}',r"ö")\
    .replace(r'\"{u}',r"ü")\
    .replace(r'\"a',r"ä")\
    .replace(r'\"e',r"ë")\
    .replace(r'\"i',r"ï")\
    .replace(r'\"o',r"ö")\
    .replace(r'\"u',r"ü")\
    .replace(r'\"{\a}',r"ä")\
    .replace(r'\"{\e}',r"ë")\
    .replace(r'\"{\i}',r"ï")\
    .replace(r'\"{\o}',r"ö")\
    .replace(r'\"{\u}',r"ü")\
    .replace(r'\"{A}',r"Ä")\
    .replace(r'\"{E}',r"Ë")\
    .replace(r'\"{I}',r"Ï")\
    .replace(r'\"{O}',r"Ö")\
    .replace(r'\"{U}',r"Ü")\
    .replace(r'\"A',r"Ä")\
    .replace(r'\"E',r"Ë")\
    .replace(r'\"I',r"Ï")\
    .replace(r'\"O',r"Ö")\
    .replace(r'\"U',r"Ü")\
    .replace(r'\"{\a}',r"Ä")\
    .replace(r'\"{\e}',r"Ë")\
    .replace(r'\"{\I}',r"Ï")\
    .replace(r'\"{\O}',r"Ö")\
    .replace(r'\"{\U}',r"Ü")\
    .replace(r'{\={a}}',r"ā")\
    .replace(r'{\={e}}',r"ē")\
    .replace(r'{\={i}}',r"ī")\
    .replace(r'{\={o}}',r"ō")\
    .replace(r'{\={u}}',r"ū")\
    .replace(r'{\={\a}}',r"ā")\
    .replace(r'{\={\e}}',r"ē")\
    .replace(r'{\={\i}}',r"ī")\
    .replace(r'{\={\o}}',r"ō")\
    .replace(r'{\={\u}}',r"ū")\
    .replace(r'{\= a}',r"ā")\
    .replace(r'{\= e}',r"ē")\
    .replace(r'{\= i}',r"ī")\
    .replace(r'{\= o}',r"ō")\
    .replace(r'{\= u}',r"ū")\
    .replace(r'{\=a}',r"ā")\
    .replace(r'{\=e}',r"ē")\
    .replace(r'{\=i}',r"ī")\
    .replace(r'{\=o}',r"ō")\
    .replace(r'{\=u}',r"ū")\
    .replace(r'{\={A}}',r"Ā")\
    .replace(r'{\={E}}',r"Ē")\
    .replace(r'{\={I}}',r"Ī")\
    .replace(r'{\={O}}',r"Ō")\
    .replace(r'{\={U}}',r"Ū")\
    .replace(r'{\={\a}}',r"Ā")\
    .replace(r'{\={\e}}',r"Ē")\
    .replace(r'{\={\I}}',r"Ī")\
    .replace(r'{\={\O}}',r"Ō")\
    .replace(r'{\={\U}}',r"Ū")\
    .replace(r'{\= A}',r"Ā")\
    .replace(r'{\= E}',r"Ē")\
    .replace(r'{\= I}',r"Ī")\
    .replace(r'{\= O}',r"Ō")\
    .replace(r'{\= U}',r"Ū")\
    .replace(r'{\=A}',r"Ā")\
    .replace(r'{\=E}',r"Ē")\
    .replace(r'{\=I}',r"Ī")\
    .replace(r'{\=O}',r"Ō")\
    .replace(r'{\=U}',r"Ū")\
    .replace(r'\={a}',r"ā")\
    .replace(r'\={e}',r"ē")\
    .replace(r'\={i}',r"ī")\
    .replace(r'\={o}',r"ō")\
    .replace(r'\={u}',r"ū")\
    .replace(r'\=a',r"ā")\
    .replace(r'\=e',r"ē")\
    .replace(r'\=i',r"ī")\
    .replace(r'\=o',r"ō")\
    .replace(r'\=u',r"ū")\
    .replace(r'\={\a}',r"ā")\
    .replace(r'\={\e}',r"ē")\
    .replace(r'\={\i}',r"ī")\
    .replace(r'\={\o}',r"ō")\
    .replace(r'\={\u}',r"ū")\
    .replace(r'\={A}',r"Ā")\
    .replace(r'\={E}',r"Ē")\
    .replace(r'\={I}',r"Ī")\
    .replace(r'\={O}',r"Ō")\
    .replace(r'\={U}',r"Ū")\
    .replace(r'\=A',r"Ā")\
    .replace(r'\=E',r"Ē")\
    .replace(r'\=I',r"Ī")\
    .replace(r'\=O',r"Ō")\
    .replace(r'\=U',r"Ū")\
    .replace(r'\={\a}',r"Ā")\
    .replace(r'\={\e}',r"Ē")\
    .replace(r'\={\I}',r"Ī")\
    .replace(r'\={\O}',r"Ō")\
    .replace(r'\={\U}',r"Ū")\
    .replace(r'{\.{a}}',r"ȧ")\
    .replace(r'{\.{c}}',r"ċ")\
    .replace(r'{\.{e}}',r"ė")\
    .replace(r'{\.{g}}',r"ġ")\
    .replace(r'{\.{o}}',r"ȯ")\
    .replace(r'{\.{z}}',r"ż")\
    .replace(r'{\.{\a}}',r"ȧ")\
    .replace(r'{\.{\c}}',r"ċ")\
    .replace(r'{\.{\e}}',r"ė")\
    .replace(r'{\.{\g}}',r"ġ")\
    .replace(r'{\.{\o}}',r"ȯ")\
    .replace(r'{\.{\z}}',r"ż")\
    .replace(r'{\. a}',r"ȧ")\
    .replace(r'{\. c}',r"ċ")\
    .replace(r'{\. e}',r"ė")\
    .replace(r'{\. g}',r"ġ")\
    .replace(r'{\. o}',r"ȯ")\
    .replace(r'{\. z}',r"ż")\
    .replace(r'{\.a}',r"ȧ")\
    .replace(r'{\.c}',r"ċ")\
    .replace(r'{\.e}',r"ė")\
    .replace(r'{\.g}',r"ġ")\
    .replace(r'{\.o}',r"ȯ")\
    .replace(r'{\.z}',r"ż")\
    .replace(r'{\.{A}}',r"Ȧ")\
    .replace(r'{\.{C}}',r"Ċ")\
    .replace(r'{\.{E}}',r"Ė")\
    .replace(r'{\.{G}}',r"Ġ")\
    .replace(r'{\.{O}}',r"Ȯ")\
    .replace(r'{\.{Z}}',r"Ż")\
    .replace(r'{\.{\a}}',r"Ȧ")\
    .replace(r'{\.{\c}}',r"Ċ")\
    .replace(r'{\.{\e}}',r"Ė")\
    .replace(r'{\.{\G}}',r"Ġ")\
    .replace(r'{\.{\O}}',r"Ȯ")\
    .replace(r'{\.{\Z}}',r"Ż")\
    .replace(r'{\. A}',r"Ȧ")\
    .replace(r'{\. C}',r"Ċ")\
    .replace(r'{\. E}',r"Ė")\
    .replace(r'{\. G}',r"Ġ")\
    .replace(r'{\. O}',r"Ȯ")\
    .replace(r'{\. Z}',r"Ż")\
    .replace(r'{\.A}',r"Ȧ")\
    .replace(r'{\.C}',r"Ċ")\
    .replace(r'{\.E}',r"Ė")\
    .replace(r'{\.G}',r"Ġ")\
    .replace(r'{\.O}',r"Ȯ")\
    .replace(r'{\.Z}',r"Ż")\
    .replace(r'\.{a}',r"ȧ")\
    .replace(r'\.{c}',r"ċ")\
    .replace(r'\.{e}',r"ė")\
    .replace(r'\.{g}',r"ġ")\
    .replace(r'\.{o}',r"ȯ")\
    .replace(r'\.{z}',r"ż")\
    .replace(r'\.a',r"ȧ")\
    .replace(r'\.c',r"ċ")\
    .replace(r'\.e',r"ė")\
    .replace(r'\.g',r"ġ")\
    .replace(r'\.o',r"ȯ")\
    .replace(r'\.z',r"ż")\
    .replace(r'\.{\a}',r"ȧ")\
    .replace(r'\.{\c}',r"ċ")\
    .replace(r'\.{\e}',r"ė")\
    .replace(r'\.{\g}',r"ġ")\
    .replace(r'\.{\o}',r"ȯ")\
    .replace(r'\.{\z}',r"ż")\
    .replace(r'\.{A}',r"Ȧ")\
    .replace(r'\.{C}',r"Ċ")\
    .replace(r'\.{E}',r"Ė")\
    .replace(r'\.{G}',r"Ġ")\
    .replace(r'\.{O}',r"Ȯ")\
    .replace(r'\.{Z}',r"Ż")\
    .replace(r'\.A',r"Ȧ")\
    .replace(r'\.C',r"Ċ")\
    .replace(r'\.E',r"Ė")\
    .replace(r'\.G',r"Ġ")\
    .replace(r'\.O',r"Ȯ")\
    .replace(r'\.Z',r"Ż")\
    .replace(r'\.{\a}',r"Ȧ")\
    .replace(r'\.{\c}',r"Ċ")\
    .replace(r'\.{\e}',r"Ė")\
    .replace(r'\.{\G}',r"Ġ")\
    .replace(r'\.{\O}',r"Ȯ")\
    .replace(r'\.{\Z}',r"Ż")\
    .replace(r'{\d{a}}',r"ạ")\
    .replace(r'{\d{e}}',r"ẹ")\
    .replace(r'{\d{h}}',r"ḥ")\
    .replace(r'{\d{i}}',r"ị")\
    .replace(r'{\d{m}}',r"ṃ")\
    .replace(r'{\d{n}}',r"ṇ")\
    .replace(r'{\d{o}}',r"ọ")\
    .replace(r'{\d{r}}',r"ṛ")\
    .replace(r'{\d{s}}',r"ṣ")\
    .replace(r'{\d{u}}',r"ụ")\
    .replace(r'{\d{\a}}',r"ạ")\
    .replace(r'{\d{\e}}',r"ẹ")\
    .replace(r'{\d{\h}}',r"ḥ")\
    .replace(r'{\d{\i}}',r"ị")\
    .replace(r'{\d{\m}}',r"ṃ")\
    .replace(r'{\d{\n}}',r"ṇ")\
    .replace(r'{\d{\o}}',r"ọ")\
    .replace(r'{\d{\r}}',r"ṛ")\
    .replace(r'{\d{\s}}',r"ṣ")\
    .replace(r'{\d{\u}}',r"ụ")\
    .replace(r'{\d a}',r"ạ")\
    .replace(r'{\d e}',r"ẹ")\
    .replace(r'{\d h}',r"ḥ")\
    .replace(r'{\d i}',r"ị")\
    .replace(r'{\d m}',r"ṃ")\
    .replace(r'{\d n}',r"ṇ")\
    .replace(r'{\d o}',r"ọ")\
    .replace(r'{\d r}',r"ṛ")\
    .replace(r'{\d s}',r"ṣ")\
    .replace(r'{\d u}',r"ụ")\
    .replace(r'{\da}',r"ạ")\
    .replace(r'{\de}',r"ẹ")\
    .replace(r'{\dh}',r"ḥ")\
    .replace(r'{\di}',r"ị")\
    .replace(r'{\dm}',r"ṃ")\
    .replace(r'{\dn}',r"ṇ")\
    .replace(r'{\do}',r"ọ")\
    .replace(r'{\dr}',r"ṛ")\
    .replace(r'{\ds}',r"ṣ")\
    .replace(r'{\du}',r"ụ")\
    .replace(r'{\d{A}}',r"Ạ")\
    .replace(r'{\d{E}}',r"Ẹ")\
    .replace(r'{\d{H}}',r"Ḥ")\
    .replace(r'{\d{I}}',r"Ị")\
    .replace(r'{\d{M}}',r"Ṃ")\
    .replace(r'{\d{N}}',r"Ṇ")\
    .replace(r'{\d{O}}',r"Ọ")\
    .replace(r'{\d{R}}',r"Ṛ")\
    .replace(r'{\d{S}}',r"Ṣ")\
    .replace(r'{\d{U}}',r"Ụ")\
    .replace(r'{\d{\a}}',r"Ạ")\
    .replace(r'{\d{\e}}',r"Ẹ")\
    .replace(r'{\d{\H}}',r"Ḥ")\
    .replace(r'{\d{\I}}',r"Ị")\
    .replace(r'{\d{\M}}',r"Ṃ")\
    .replace(r'{\d{\n}}',r"Ṇ")\
    .replace(r'{\d{\O}}',r"Ọ")\
    .replace(r'{\d{\r}}',r"Ṛ")\
    .replace(r'{\d{\S}}',r"Ṣ")\
    .replace(r'{\d{\U}}',r"Ụ")\
    .replace(r'{\d A}',r"Ạ")\
    .replace(r'{\d E}',r"Ẹ")\
    .replace(r'{\d H}',r"Ḥ")\
    .replace(r'{\d I}',r"Ị")\
    .replace(r'{\d M}',r"Ṃ")\
    .replace(r'{\d N}',r"Ṇ")\
    .replace(r'{\d O}',r"Ọ")\
    .replace(r'{\d R}',r"Ṛ")\
    .replace(r'{\d S}',r"Ṣ")\
    .replace(r'{\d U}',r"Ụ")\
    .replace(r'{\dA}',r"Ạ")\
    .replace(r'{\dE}',r"Ẹ")\
    .replace(r'{\dH}',r"Ḥ")\
    .replace(r'{\dI}',r"Ị")\
    .replace(r'{\dM}',r"Ṃ")\
    .replace(r'{\dN}',r"Ṇ")\
    .replace(r'{\dO}',r"Ọ")\
    .replace(r'{\dR}',r"Ṛ")\
    .replace(r'{\dS}',r"Ṣ")\
    .replace(r'{\dU}',r"Ụ")\
    .replace(r'\d{a}',r"ạ")\
    .replace(r'\d{e}',r"ẹ")\
    .replace(r'\d{h}',r"ḥ")\
    .replace(r'\d{i}',r"ị")\
    .replace(r'\d{m}',r"ṃ")\
    .replace(r'\d{n}',r"ṇ")\
    .replace(r'\d{o}',r"ọ")\
    .replace(r'\d{r}',r"ṛ")\
    .replace(r'\d{s}',r"ṣ")\
    .replace(r'\d{u}',r"ụ")\
    .replace(r'\da',r"ạ")\
    .replace(r'\de',r"ẹ")\
    .replace(r'\dh',r"ḥ")\
    .replace(r'\di',r"ị")\
    .replace(r'\dm',r"ṃ")\
    .replace(r'\dn',r"ṇ")\
    .replace(r'\do',r"ọ")\
    .replace(r'\dr',r"ṛ")\
    .replace(r'\ds',r"ṣ")\
    .replace(r'\du',r"ụ")\
    .replace(r'\d{\a}',r"ạ")\
    .replace(r'\d{\e}',r"ẹ")\
    .replace(r'\d{\h}',r"ḥ")\
    .replace(r'\d{\i}',r"ị")\
    .replace(r'\d{\m}',r"ṃ")\
    .replace(r'\d{\n}',r"ṇ")\
    .replace(r'\d{\o}',r"ọ")\
    .replace(r'\d{\r}',r"ṛ")\
    .replace(r'\d{\s}',r"ṣ")\
    .replace(r'\d{\u}',r"ụ")\
    .replace(r'\d{A}',r"Ạ")\
    .replace(r'\d{E}',r"Ẹ")\
    .replace(r'\d{H}',r"Ḥ")\
    .replace(r'\d{I}',r"Ị")\
    .replace(r'\d{M}',r"Ṃ")\
    .replace(r'\d{N}',r"Ṇ")\
    .replace(r'\d{O}',r"Ọ")\
    .replace(r'\d{R}',r"Ṛ")\
    .replace(r'\d{S}',r"Ṣ")\
    .replace(r'\d{U}',r"Ụ")\
    .replace(r'\dA',r"Ạ")\
    .replace(r'\dE',r"Ẹ")\
    .replace(r'\dH',r"Ḥ")\
    .replace(r'\dI',r"Ị")\
    .replace(r'\dM',r"Ṃ")\
    .replace(r'\dN',r"Ṇ")\
    .replace(r'\dO',r"Ọ")\
    .replace(r'\dR',r"Ṛ")\
    .replace(r'\dS',r"Ṣ")\
    .replace(r'\dU',r"Ụ")\
    .replace(r'\d{\a}',r"Ạ")\
    .replace(r'\d{\e}',r"Ẹ")\
    .replace(r'\d{\H}',r"Ḥ")\
    .replace(r'\d{\I}',r"Ị")\
    .replace(r'\d{\M}',r"Ṃ")\
    .replace(r'\d{\n}',r"Ṇ")\
    .replace(r'\d{\O}',r"Ọ")\
    .replace(r'\d{\r}',r"Ṛ")\
    .replace(r'\d{\S}',r"Ṣ")\
    .replace(r'\d{\U}',r"Ụ")\
    .replace(r'{\u{a}}',r"ă")\
    .replace(r'{\u{e}}',r"ĕ")\
    .replace(r'{\u{g}}',r"ğ")\
    .replace(r'{\u{i}}',r"ĭ")\
    .replace(r'{\u{o}}',r"ŏ")\
    .replace(r'{\u{u}}',r"ŭ")\
    .replace(r'{\u{\a}}',r"ă")\
    .replace(r'{\u{\e}}',r"ĕ")\
    .replace(r'{\u{\g}}',r"ğ")\
    .replace(r'{\u{\i}}',r"ĭ")\
    .replace(r'{\u{\o}}',r"ŏ")\
    .replace(r'{\u{\u}}',r"ŭ")\
    .replace(r'{\u a}',r"ă")\
    .replace(r'{\u e}',r"ĕ")\
    .replace(r'{\u g}',r"ğ")\
    .replace(r'{\u i}',r"ĭ")\
    .replace(r'{\u o}',r"ŏ")\
    .replace(r'{\u u}',r"ŭ")\
    .replace(r'{\ua}',r"ă")\
    .replace(r'{\ue}',r"ĕ")\
    .replace(r'{\ug}',r"ğ")\
    .replace(r'{\ui}',r"ĭ")\
    .replace(r'{\uo}',r"ŏ")\
    .replace(r'{\uu}',r"ŭ")\
    .replace(r'{\u{A}}',r"Ă")\
    .replace(r'{\u{E}}',r"Ĕ")\
    .replace(r'{\u{G}}',r"Ğ")\
    .replace(r'{\u{I}}',r"Ĭ")\
    .replace(r'{\u{O}}',r"Ŏ")\
    .replace(r'{\u{U}}',r"Ŭ")\
    .replace(r'{\u{\a}}',r"Ă")\
    .replace(r'{\u{\e}}',r"Ĕ")\
    .replace(r'{\u{\G}}',r"Ğ")\
    .replace(r'{\u{\I}}',r"Ĭ")\
    .replace(r'{\u{\O}}',r"Ŏ")\
    .replace(r'{\u{\U}}',r"Ŭ")\
    .replace(r'{\u A}',r"Ă")\
    .replace(r'{\u E}',r"Ĕ")\
    .replace(r'{\u G}',r"Ğ")\
    .replace(r'{\u I}',r"Ĭ")\
    .replace(r'{\u O}',r"Ŏ")\
    .replace(r'{\u U}',r"Ŭ")\
    .replace(r'{\uA}',r"Ă")\
    .replace(r'{\uE}',r"Ĕ")\
    .replace(r'{\uG}',r"Ğ")\
    .replace(r'{\uI}',r"Ĭ")\
    .replace(r'{\uO}',r"Ŏ")\
    .replace(r'{\uU}',r"Ŭ")\
    .replace(r'\u{a}',r"ă")\
    .replace(r'\u{e}',r"ĕ")\
    .replace(r'\u{g}',r"ğ")\
    .replace(r'\u{i}',r"ĭ")\
    .replace(r'\u{o}',r"ŏ")\
    .replace(r'\u{u}',r"ŭ")\
    .replace(r'\ua',r"ă")\
    .replace(r'\ue',r"ĕ")\
    .replace(r'\ug',r"ğ")\
    .replace(r'\ui',r"ĭ")\
    .replace(r'\uo',r"ŏ")\
    .replace(r'\uu',r"ŭ")\
    .replace(r'\u{\a}',r"ă")\
    .replace(r'\u{\e}',r"ĕ")\
    .replace(r'\u{\g}',r"ğ")\
    .replace(r'\u{\i}',r"ĭ")\
    .replace(r'\u{\o}',r"ŏ")\
    .replace(r'\u{\u}',r"ŭ")\
    .replace(r'\u{A}',r"Ă")\
    .replace(r'\u{E}',r"Ĕ")\
    .replace(r'\u{G}',r"Ğ")\
    .replace(r'\u{I}',r"Ĭ")\
    .replace(r'\u{O}',r"Ŏ")\
    .replace(r'\u{U}',r"Ŭ")\
    .replace(r'\uA',r"Ă")\
    .replace(r'\uE',r"Ĕ")\
    .replace(r'\uG',r"Ğ")\
    .replace(r'\uI',r"Ĭ")\
    .replace(r'\uO',r"Ŏ")\
    .replace(r'\uU',r"Ŭ")\
    .replace(r'\u{\a}',r"Ă")\
    .replace(r'\u{\e}',r"Ĕ")\
    .replace(r'\u{\G}',r"Ğ")\
    .replace(r'\u{\I}',r"Ĭ")\
    .replace(r'\u{\O}',r"Ŏ")\
    .replace(r'\u{\U}',r"Ŭ")\
    .replace(r'{\H{o}}',r"ő")\
    .replace(r'{\H{u}}',r"ű")\
    .replace(r'{\H{\o}}',r"ő")\
    .replace(r'{\H{\u}}',r"ű")\
    .replace(r'{\H o}',r"ő")\
    .replace(r'{\H u}',r"ű")\
    .replace(r'{\Ho}',r"ő")\
    .replace(r'{\Hu}',r"ű")\
    .replace(r'{\H{O}}',r"Ő")\
    .replace(r'{\H{U}}',r"Ű")\
    .replace(r'{\H{\O}}',r"Ő")\
    .replace(r'{\H{\U}}',r"Ű")\
    .replace(r'{\H O}',r"Ő")\
    .replace(r'{\H U}',r"Ű")\
    .replace(r'{\HO}',r"Ő")\
    .replace(r'{\HU}',r"Ű")\
    .replace(r'\H{o}',r"ő")\
    .replace(r'\H{u}',r"ű")\
    .replace(r'\Ho',r"ő")\
    .replace(r'\Hu',r"ű")\
    .replace(r'\H{\o}',r"ő")\
    .replace(r'\H{\u}',r"ű")\
    .replace(r'\H{O}',r"Ő")\
    .replace(r'\H{U}',r"Ű")\
    .replace(r'\HO',r"Ő")\
    .replace(r'\HU',r"Ű")\
    .replace(r'\H{\O}',r"Ő")\
    .replace(r'\H{\U}',r"Ű")\
    .replace(r'a{\v}',r"â")\
    .replace(r'A{\v}',r"Â")\
    .replace(r'{\v{a}}',r"ǎ")\
    .replace(r'{\v{\a}}',r"ǎ")\
    .replace(r'{\v a}',r"ǎ")\
    .replace(r'{\va}',r"ǎ")\
    .replace(r'\v{a}',r"ǎ")\
    .replace(r'\va',r"ǎ")\
    .replace(r'\v{\a}',r"ǎ")\
    .replace(r'{\v{A}}',r"Ǎ")\
    .replace(r'{\v{\a}}',r"Ǎ")\
    .replace(r'{\v A}',r"Ǎ")\
    .replace(r'{\vA}',r"Ǎ")\
    .replace(r'\v{A}',r"Ǎ")\
    .replace(r'\vA',r"Ǎ")\
    .replace(r'\v{\a}',r"Ǎ")\
    .replace(r'{\v{c}}',r"č")\
    .replace(r'{\v{\c}}',r"č")\
    .replace(r'{\v c}',r"č")\
    .replace(r'{\vc}',r"č")\
    .replace(r'\v{c}',r"č")\
    .replace(r'\vc',r"č")\
    .replace(r'\v{\c}',r"č")\
    .replace(r'{\v{C}}',r"Č")\
    .replace(r'{\v{\c}}',r"Č")\
    .replace(r'{\v C}',r"Č")\
    .replace(r'{\vC}',r"Č")\
    .replace(r'\v{C}',r"Č")\
    .replace(r'\vC',r"Č")\
    .replace(r'\v{\c}',r"Č")\
    .replace(r'e{\v}',r"ê")\
    .replace(r'{\v{e}}',r"ě")\
    .replace(r'{\v{\e}}',r"ě")\
    .replace(r'{\v e}',r"ě")\
    .replace(r'{\ve}',r"ě")\
    .replace(r'\v{e}',r"ě")\
    .replace(r'\ve',r"ě")\
    .replace(r'\v{\e}',r"ě")\
    .replace(r'E{\v}',r"Ê")\
    .replace(r'{\v{E}}',r"Ě")\
    .replace(r'{\v{\e}}',r"Ě")\
    .replace(r'{\v E}',r"Ě")\
    .replace(r'{\vE}',r"Ě")\
    .replace(r'\v{E}',r"Ě")\
    .replace(r'\vE',r"Ě")\
    .replace(r'\v{\e}',r"Ě")\
    .replace(r'{\v{j}}',r"ǰ")\
    .replace(r'{\v{\j}}',r"ǰ")\
    .replace(r'{\v j}',r"ǰ")\
    .replace(r'{\vj}',r"ǰ")\
    .replace(r'\v{j}',r"ǰ")\
    .replace(r'\vj',r"ǰ")\
    .replace(r'\v{\j}',r"ǰ")\
    .replace(r'{\v{r}}',r"ř")\
    .replace(r'{\v{\r}}',r"ř")\
    .replace(r'{\v r}',r"ř")\
    .replace(r'{\vr}',r"ř")\
    .replace(r'\v{r}',r"ř")\
    .replace(r'\vr',r"ř")\
    .replace(r'\v{\r}',r"ř")\
    .replace(r'{\v{R}}',r"Ř")\
    .replace(r'{\v{\r}}',r"Ř")\
    .replace(r'{\v R}}',r"Ř")\
    .replace(r'{\vR}}',r"Ř")\
    .replace(r'\v{R}',r"Ř")\
    .replace(r'\vR',r"Ř")\
    .replace(r'\v{\r}',r"Ř")\
    .replace(r'{\v{s}}',r"š")\
    .replace(r'{\v{\s}}',r"š")\
    .replace(r'{\v s}',r"š")\
    .replace(r'{\vs}',r"š")\
    .replace(r'\v{s}',r"š")\
    .replace(r'\vs',r"š")\
    .replace(r'\v{\s}',r"š")\
    .replace(r'{\v{S}}',r"Š")\
    .replace(r'{\v S}',r"Š")\
    .replace(r'{\vS}',r"Š")\
    .replace(r'{\v{\S}}',r"Š")\
    .replace(r'\v{S}',r"Š")\
    .replace(r'\vS',r"Š")\
    .replace(r'\v{\S}',r"Š")\
    .replace(r'{\v{z}}',r"ž")\
    .replace(r'{\v{\z}}',r"ž")\
    .replace(r'{\v z}',r"ž")\
    .replace(r'{\vz}',r"ž")\
    .replace(r'\v{z}',r"ž")\
    .replace(r'\vz',r"ž")\
    .replace(r'\v{\z}',r"ž")\
    .replace(r'{\v{Z}}',r"Ž")\
    .replace(r'{\v{\Z}}',r"Ž")\
    .replace(r'{\v Z}',r"Ž")\
    .replace(r'{\vZ}',r"Ž")\
    .replace(r'\v{Z}',r"Ž")\
    .replace(r'\vZ',r"Ž")\
    .replace(r'\v{\Z}',r"Ž")\
    .replace(r'{\c{s}}',r"ş")\
    .replace(r'{\c{\s}}',r"ş")\
    .replace(r'{\c s}',r"ş")\
    .replace(r'\c{s}',r"ş")\
    .replace(r'\cs',r"ş")\
    .replace(r'\c{\s}',r"ş")\
    .replace(r's{\c}',r"ş")\
    .replace(r's{c}',r"ş")\
    .replace(r'{\c{S}}',r"Ş")\
    .replace(r'{\c{\S}}',r"Ş")\
    .replace(r'{\c S}',r"Ş")\
    .replace(r'{\cS}',r"Ş")\
    .replace(r'\c{S}',r"Ş")\
    .replace(r'\cS',r"Ş")\
    .replace(r'\c{\S}',r"Ş")\
    .replace(r'S{\c}',r"Ş")\
    .replace(r'S{c}',r"Ş")\
    .replace(r'{\c{e}}',r"ȩ")\
    .replace(r'{\c{\e}}',r"ȩ")\
    .replace(r'{\c e}',r"ȩ")\
    .replace(r'{\ce}',r"ȩ")\
    .replace(r'\c{e}',r"ȩ")\
    .replace(r'\ce',r"ȩ")\
    .replace(r'\c{\e}',r"ȩ")\
    .replace(r'e{\c}',r"ȩ")\
    .replace(r'e{c}',r"ȩ")\
    .replace(r'{\c{E}}',r"Ȩ")\
    .replace(r'{\c{\e}}',r"Ȩ")\
    .replace(r'{\c E}',r"Ȩ")\
    .replace(r'{\cE}',r"Ȩ")\
    .replace(r'\c{E}',r"Ȩ")\
    .replace(r'\cE',r"Ȩ")\
    .replace(r'\c{\e}',r"Ȩ")\
    .replace(r'E{\c}',r"Ȩ")\
    .replace(r'E{c}',r"Ȩ")\
    .replace(r'{\c{c}}',r"ç")\
    .replace(r'{\c{\c}}',r"ç")\
    .replace(r'{\c c}',r"ç")\
    .replace(r'{\cc}',r"ç")\
    .replace(r'\c{c}',r"ç")\
    .replace(r'\cc',r"ç")\
    .replace(r'\c{\c}',r"ç")\
    .replace(r'c{\c}',r"ç")\
    .replace(r'c{c}',r"ç")\
    .replace(r'{\c{C}}',r"Ç")\
    .replace(r'{\c{\c}}',r"Ç")\
    .replace(r'{\c C}',r"Ç")\
    .replace(r'{\cC}',r"Ç")\
    .replace(r'\c{C}',r"Ç")\
    .replace(r'\cC',r"Ç")\
    .replace(r'\c{\c}',r"Ç")\
    .replace(r'C{\c}',r"Ç")\
    .replace(r'C{c}',r"Ç")\
    .replace(r'{\~{a}}',r"ã")\
    .replace(r'{\~{o}}',r"õ")\
    .replace(r'{\~{\a}}',r"ã")\
    .replace(r'{\~{\o}}',r"õ")\
    .replace(r'{\~ a}',r"ã")\
    .replace(r'{\~ o}',r"õ")\
    .replace(r'{\~a}',r"ã")\
    .replace(r'{\~o}',r"õ")\
    .replace(r'{\~{A}}',r"Ã")\
    .replace(r'{\~{O}}',r"Õ")\
    .replace(r'{\~{\a}}',r"Ã")\
    .replace(r'{\~{\O}}',r"Õ")\
    .replace(r'{\~ A}',r"Ã")\
    .replace(r'{\~ O}',r"Õ")\
    .replace(r'{\~A}',r"Ã")\
    .replace(r'{\~O}',r"Õ")\
    .replace(r'\~{a}',r"ã")\
    .replace(r'\~{o}',r"õ")\
    .replace(r'\~a',r"ã")\
    .replace(r'\~o',r"õ")\
    .replace(r'\~{\a}',r"ã")\
    .replace(r'\~{\o}',r"õ")\
    .replace(r'\~{A}',r"Ã")\
    .replace(r'\~{O}',r"Õ")\
    .replace(r'\~A',r"Ã")\
    .replace(r'\~O',r"Õ")\
    .replace(r'\~{\a}',r"Ã")\
    .replace(r'\~{\O}',r"Õ")\
    .replace(r'{\~{n}}',r"ñ")\
    .replace(r'{\~{\n}}',r"ñ")\
    .replace(r'{\~ n}',r"ñ")\
    .replace(r'{\~n}',r"ñ")\
    .replace(r'\~{n}',r"ñ")\
    .replace(r'\~n',r"ñ")\
    .replace(r'\~{\n}',r"ñ")\
    .replace(r'{\~{N}}',r"Ñ")\
    .replace(r'{\~{\n}}',r"Ñ")\
    .replace(r'{\~ N}',r"Ñ")\
    .replace(r'{\~N}',r"Ñ")\
    .replace(r'\~{N}',r"Ñ")\
    .replace(r'\~N',r"Ñ")\
    .replace(r'\~{\n}',r"Ñ")\
    .replace(r'{\aa}',r"å")\
    .replace(r'\aa',r"å")\
    .replace(r'{\aA}',r"Å")\
    .replace(r'\aA',r"Å")\
    .replace(r'{\r{a}}',r"å")\
    .replace(r'{\r{\a}}',r"å")\
    .replace(r'{\r a}',r"å")\
    .replace(r'{\ra}',r"å")\
    .replace(r'\r{a}',r"å")\
    .replace(r'\ra',r"å")\
    .replace(r'\r{\a}',r"å")\
    .replace(r'{\r{A}}',r"Å")\
    .replace(r'{\r{\a}}',r"Å")\
    .replace(r'{\r A}',r"Å")\
    .replace(r'{\rA}',r"Å")\
    .replace(r'\r{A}',r"Å")\
    .replace(r'\rA',r"Å")\
    .replace(r'\r{\a}',r"Å")\
    .replace(r'{\r{u}}',r"ů")\
    .replace(r'{\r{\u}}',r"ů")\
    .replace(r'{\r u}',r"ů")\
    .replace(r'{\ru}',r"ů")\
    .replace(r'\r{u}',r"ů")\
    .replace(r'\ru',r"ů")\
    .replace(r'\r{\u}',r"ů")\
    .replace(r'{\r{U}}',r"Ů")\
    .replace(r'{\r{\U}}',r"Ů")\
    .replace(r'{\r U}',r"Ů")\
    .replace(r'{\rU}',r"Ů")\
    .replace(r'\r{U}',r"Ů")\
    .replace(r'\rU',r"Ů")\
    .replace(r'\r{\U}',r"Ů")\
    .replace(r'{\ae}',r"æ")\
    .replace(r'\ae',r"æ")\
    .replace(r'{\aE}',r"Æ")\
    .replace(r'\aE',r"Æ")\
    .replace(r'{\oe}',r"œ")\
    .replace(r'\oe',r"œ")\
    .replace(r'{\OE}',r"Œ")\
    .replace(r'\OE',r"Œ")\
    .replace(r'{\o}',r"ø")\
    .replace(r'\o',r"ø")\
    .replace(r'\o{}',r"ø")\
    .replace(r'{\O}',r"Ø")\
    .replace(r'\O',r"Ø")\
    .replace(r'\O{}',r"Ø")\
    .replace(r'{\ss}',r"ß")\
    .replace(r'\ss',r"ß")\
    .replace(r'{\l}',r"ł")\
    .replace(r'\l',r"ł")\
    .replace(r'{\L}',r"Ł")\
    .replace(r'\L',r"Ł")\
    .replace(r'{\i}',r"ı")\
    .replace(r'\i',r"ı")\
    .replace(r'{\textquotesingle}',r"'")\
    .replace(r'\textquotesingle',r"'")\
    .replace(r'{\textendash}',r"–")\
    .replace(r'\textendash',r"–")\
    .replace(r'{\textemdash}',r"—")\
    .replace(r'\textemdash',r"—")\
    .replace(r'{\textgreater}',r">")\
    .replace(r'\textgreater',r">")\
    .replace(r'{\textless}',r"<")\
    .replace(r'\textless',r"<")\
    .replace(r'{\textquoteright}',r"'")\
    .replace(r'\textquoteright',r"'")\
    .replace(r'{\textquoteleft}',r"'")\
    .replace(r'\textquoteleft',r"'")\
    .replace(r'{\textquotedblright}',r'"')\
    .replace(r'\textquotedblright',r'"')\
    .replace(r'{\textquotedblleft}',r'"')\
    .replace(r'\textquotedblleft',r'"')\
    .replace(r"{\\",r"")\
    .replace("{\\","")\
    .replace(r'}',r'')
    return new_text