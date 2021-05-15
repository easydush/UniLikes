import React, { useCallback } from 'react';
import { Content, Header } from 'antd/lib/layout/layout';
import { Badge, Layout, Menu } from 'antd';
import { theme } from '../../styles';
import { QuestionCircleOutlined, UserOutlined } from '@ant-design/icons';
import { Link, useHistory } from 'react-router-dom';
import { MenuInfo } from 'rc-menu/lib/interface';
import { Routes as R } from '../../constants';

enum MenuKeys {
    VOTE = 'vote',
    PROFILE = 'profile',
    TEACHER_RATING = 'teacher-rating',
}

export const Main = (): JSX.Element => {
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

    return (
        <Layout>
            <Header style={{ backgroundColor: 'white' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                    <div>UniLikes</div>
                    <div style={{ width: '65%' }}>
                        <Menu mode="horizontal" defaultSelectedKeys={[MenuKeys.TEACHER_RATING]} onClick={handleChange}>
                            <Menu.Item key={MenuKeys.TEACHER_RATING}>Рейтинг преподавателей</Menu.Item>
                            <Menu.Item key={MenuKeys.PROFILE}>Профиль</Menu.Item>
                            <Menu.Item key={MenuKeys.VOTE}>
                                <Badge dot>Голосовать</Badge>
                            </Menu.Item>
                        </Menu>
                    </div>
                    <div>
                        <QuestionCircleOutlined />
                        <UserOutlined />
                        Name Surname
                        <Link to="">Выход</Link>
                    </div>
                </div>
            </Header>
            <Content style={{ backgroundColor: theme.colors.gray_3 }}>
                TODO
            </Content>
        </Layout>
    );
};
