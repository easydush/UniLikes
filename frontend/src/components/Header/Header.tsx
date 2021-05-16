import { Avatar, Badge, Menu } from 'antd';
import { QuestionCircleOutlined } from '@ant-design/icons';
import { Link, useHistory } from 'react-router-dom';
import React, { useCallback, useMemo } from 'react';
import { MenuInfo } from 'rc-menu/lib/interface';
import { Routes as R } from '../../constants';
import {
    ExitText,
    HeaderWrapper,
    InfoWrapper,
    LogoText,
    MenuWrapper,
    NameText,
    StyledHeader,
    UserBlock,
} from './styles';

enum MenuKeys {
    VOTE = 'vote',
    PROFILE = 'profile',
    TEACHER_RATING = 'teacher-rating',
}

export const HeaderCustom = (): JSX.Element => {
    const history = useHistory();

    const handleChange = useCallback(
        (info: MenuInfo) => {
            const key = info.key;
            if (key === MenuKeys.VOTE) {
                history.push(R.VOTE);
            }
            if (key === MenuKeys.TEACHER_RATING) {
                history.push(R.TEACHER_RATING);
            }
            if (key === MenuKeys.PROFILE) {
                history.push(R.PROFILE);
            }
        },
        [history],
    );
    const urlName = window.location.pathname;

    const selectedItem = useMemo(() => {
        const newUrl = urlName;

        if (newUrl === R.TEACHER_RATING || urlName === R.ROOT) {
            return MenuKeys.TEACHER_RATING;
        }
        if (newUrl === R.PROFILE) {
            return MenuKeys.PROFILE;
        }
        if (newUrl === R.VOTE) {
            return MenuKeys.VOTE;
        }

        return MenuKeys.TEACHER_RATING;
    }, [urlName]);

    return (
        <StyledHeader>
            <HeaderWrapper>
                <LogoText>UniLikes</LogoText>
                <MenuWrapper>
                    <Menu mode="horizontal" defaultSelectedKeys={[selectedItem]} onClick={handleChange}>
                        <Menu.Item key={MenuKeys.TEACHER_RATING}>Рейтинг преподавателей</Menu.Item>
                        <Menu.Item key={MenuKeys.PROFILE}>Профиль</Menu.Item>
                        <Menu.Item key={MenuKeys.VOTE}>
                            <Badge dot>Голосовать</Badge>
                        </Menu.Item>
                    </Menu>
                </MenuWrapper>
                <InfoWrapper>
                    <div>
                        <QuestionCircleOutlined />
                    </div>
                    <UserBlock>
                        <Avatar src="https://www.noku.io/file/2018/01/icon_Marketing.png" />
                        <NameText>Name Surname</NameText>
                    </UserBlock>
                    <div>
                        <Link to="">
                            <ExitText>Выход </ExitText>
                        </Link>
                    </div>
                </InfoWrapper>
            </HeaderWrapper>
        </StyledHeader>
    );
};
