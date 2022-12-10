import pytest

import temp


def get_checklist():
    initial_text = """
    Input: 'a|a'     Output: True
    Input: '.|a'     Output: True
    Input:  '|a'     Output: True
    Input:  '|'      Output: True
    Input: 'a|'      Output: False
    Input: 'apple|apple'     Output: True
    Input: '.pple|apple'     Output: True
    Input: 'appl.|apple'     Output: True
    Input: '.....|apple'     Output: True
    Input: 'peach|apple'     Output: False
    Input: 'apple|apple'     Output: True
    Input:    'ap|apple'     Output: True
    Input:    'le|apple'     Output: True
    Input:     'a|apple'     Output: True
    Input:     '.|apple'     Output: True
    Input: 'apwle|apple'     Output: False
    Input: 'peach|apple'     Output: False
    Input:    '^app|apple'           Output: True
    Input:     'le$|apple'           Output: True
    Input:      '^a|apple'           Output: True
    Input:      '.$|apple'           Output: True
    Input:  'apple$|tasty apple'     Output: True
    Input:  '^apple|apple pie'       Output: True
    Input: '^apple$|apple'           Output: True
    Input: '^apple$|tasty apple'     Output: False
    Input: '^apple$|apple pie'       Output: False
    Input:    'app$|apple'           Output: False
    Input:     '^le|apple'           Output: False
    Input:     'colour|colouur'      Output: False
    Input: 'colou?r|color'       Output: True
    Input: 'colou?r|colour'      Output: True
    Input: 'colou?r|colouur'     Output: False
    Input: 'colou*r|color'       Output: True
    Input: 'colou*r|colour'      Output: True
    Input: 'colou*r|colouur'     Output: True
    Input:  'col.*r|color'       Output: True
    Input:  'col.*r|colour'      Output: True
    Input:  'col.*r|colr'        Output: True
    Input:  'col.*r|collar'      Output: True
    Input: 'col.*r$|colors'      Output: False
    Input:  'a+b|ab'      Output: True
    Input:  'a+b|bb'        Output: False
    Input:  'a+b|aaaaaaaaab'      Output: True
    Input: 'a+b|bbbbbbbbbb'      Output: False
    Input: 'a+b|ehjwdgaabeidhew' Output: True
    Input: 'ehjwdga+b|ehjwdgaaabeidhew' Output: True
    """
    lines = initial_text.strip().split("\n")
    output_list = []
    for i in lines:
        if "True" in i:
            output = True
        elif "False" in i:
            output = False
        parts = i.split("'")
        regex, text = parts[1].split("|")
        output_list.append((regex, text, output))
    return output_list


@pytest.mark.parametrize("regex,text,output", get_checklist())
def test_menu(regex, text, output):
    assert temp.menu(regex, text, regex) == output
