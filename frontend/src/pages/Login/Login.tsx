import React from 'react';
import {
    LoginFormWrapper,
    LoginPageWrapper,
    LogoText,
    LogoTextDescription,
    LogoTextWrapper,
    TabsWrapper,
} from './styles';
import { LoginForm } from '../../components/LoginForm';
import { Tabs } from 'antd';

const { TabPane } = Tabs;
export const Login = (): JSX.Element => {


    return (
        <LoginPageWrapper>
            <LogoTextWrapper>
                <LogoText>
                    UniLikes
                </LogoText>
                <LogoTextDescription>
                    Анонимное оценивание работы преподавателей
                </LogoTextDescription>
            </LogoTextWrapper>
            <LoginFormWrapper>
                <TabsWrapper>
                    <Tabs defaultActiveKey="login">
                        <TabPane tab="Вход" key="login">
                            <LoginForm />
                        </TabPane>
                        <TabPane tab="Регистрация" key="registration">
                            Регистрация
                        </TabPane>
                    </Tabs>
                </TabsWrapper>
            </LoginFormWrapper>
        </LoginPageWrapper>
    );
};
