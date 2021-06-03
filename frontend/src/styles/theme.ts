const colors = {
    //Daybreak Blue
    blue_1: '#E6F7FF',
    blue_2: '#BAE7FF',
    blue_3: '#91D5FF',
    blue_4: '#69C0FF',
    blue_5: '#40A9FF',
    blue_6: '#1890FF',
    blue_7: '#096DD9',
    blue_8: '#0050B3',
    blue_9: '#003A8C',
    blue_10: '#002766',
    blue_11: '#011B4A',
    blue_115: '#808DA4',
    //Neutral Color Palette
    gray_1: '#FFFFFF',
    gray_2: '#FAFAFA',
    gray_3: '#F5F5F5',
    gray_35: '#F3F3F3',
    gray_4: '#E8E8E8',
    gray_5: '#D9D9D9',
    gray_6: '#BFBFBF',
    gray_7: '#8C8C8C',
    gray_8: '#595959',
    gray_9: '#262626',
    gray_95: '#151B25',
    gray_10: '#000000',
    //dust red
    red_1: '#fff1f0',
    red_2: '#ffccc7',
    red_3: '#ffa39e',
    red_4: '#ff7875',
    red_5: '#ff4d4f',
    red_6: '#f5222d',
    red_7: '#cf1322',
    red_8: '#a8071a',
    red_9: '#820014',
    red_10: '#5c0011',
    //volcano
    volcano_1: '#fff2e8',
    volcano_2: '#ffd8bf',
    volcano_3: '#ffbb96',
    volcano_4: '#ff9c6e',
    volcano_5: '#ff7a45',
    volcano_6: '#fa541c',
    volcano_7: '#d4380d',
    volcano_8: '#ad2102',
    volcano_9: '#871400',
    volcano_10: '#610b00',
    //sunset orange
    orange_1: '#fff7e6',
    orange_2: '#ffe7ba',
    orange_3: '#ffd591',
    orange_4: '#ffc069',
    orange_5: '#ffa940',
    orange_6: '#fa8c16',
    orange_7: '#d46b08',
    orange_8: '#ad4e00',
    orange_9: '#873800',
    orange_10: '#612500',
    //polar green
    green_1: '#f6ffed',
    green_2: '#d9f7be',
    green_3: '#b7eb8f',
    green_4: '#95de64',
    green_5: '#73d13d',
    green_6: '#52c41a',
    green_7: '#389e0d',
    green_8: '#237804',
    green_9: '#135200',
    green_10: '#092b00',
};

const elements = {
    TEXT_PRIMARY: colors.blue_11,
    TEXT_SECONDARY: colors.blue_115,
    BG: colors.gray_3,

    GREY_INPUT: colors.gray_3,
    BORDER_GREY: colors.gray_4,

    BUTTON_PRIMARY: colors.orange_6,
    BUTTON_PRIMARY_HOVER: colors.orange_7,

    BUTTON_BLUE_OUTLINE: colors.blue_6,

    SUCCESS: colors.green_6,

    BLUE_BOX_SHADOW: '0px 0px 12px rgba(4, 22, 54, 0.12)',
};

type StyleTheme = {
    colors: { [key in keyof typeof colors]: string };
    elements: { [key in keyof typeof elements]: string };
};

const theme: StyleTheme = {
    colors,
    elements,
};

export { theme };
