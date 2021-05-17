import { Form, Input } from 'antd';
import { makeRequiredFormFieldRule } from '../../utils/formRules';
import React, { useCallback, useState } from 'react';
import { register } from '../../api';
import { setEmail } from '../../utils';
import { LockIcon, SubmitButton, UserIcon } from './styles';
import { useHistory } from 'react-router-dom';
import { Routes as R } from '../../constants';
import { isSuccessful } from '../../api/helpers';

export const RegisterForm = (): JSX.Element => {

    const [loading, setLoading] = useState<boolean>(false);
    const history = useHistory();

    const handleFinish = useCallback(async (values) => {
        setLoading(true);
        await register(values);
        history.push(R.ACTIVATION);

        setLoading(false);
    }, [history]);

    return (
        <Form onFinish={handleFinish}>
            <Form.Item
                name='name'
                rules={[makeRequiredFormFieldRule('Please input your name!')]}
            >
                <Input
                    prefix={<UserIcon className='site-form-item-icon' />}
                    placeholder='Имя пользователя'
                />
            </Form.Item>

            <Form.Item
                name='email'
                rules={[makeRequiredFormFieldRule('Please input your email!')]}
            >
                <Input
                    prefix={<UserIcon className='site-form-item-icon' />}
                    placeholder='example@stud.kpfu.ru'
                />
            </Form.Item>

            <Form.Item
                name='password'
                rules={[{ required: true, message: 'Please input your password!' }]}
            >
                <Input
                    prefix={<LockIcon className='site-form-item-icon' />}
                    type='password'
                    placeholder='Пароль'
                />
            </Form.Item>
            <Form.Item
                name='re_password'
                rules={[{ required: true, message: 'Please repeat your password!' }]}
            >
                <Input
                    prefix={<LockIcon className='site-form-item-icon' />}
                    type='password'
                    placeholder='Повторение пароля'
                />
            </Form.Item>

            <Form.Item>
                <SubmitButton type='primary' htmlType='submit' loading={loading}>
                    Вход
                </SubmitButton>
            </Form.Item>
        </Form>
    );
};
