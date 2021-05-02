import React, { useCallback } from 'react';
import { Button, Form, Input } from 'antd';
import { authorize } from '../../api';

export const Login = (): JSX.Element => {

    const handleFinish = useCallback((values) => {
        authorize(values);
    }, []);

    return (
        <Form onFinish={handleFinish}>
            <Form.Item
                label='Email'
                name='email'
                rules={[{ required: true, message: 'Please input your email!' }]}
            >
                <Input />
            </Form.Item>

            <Form.Item
                label='Password'
                name='password'
                rules={[{ required: true, message: 'Please input your password!' }]}
            >
                <Input.Password />
            </Form.Item>

            <Form.Item>
                <Button type='primary' htmlType='submit'>
                    Submit
                </Button>
            </Form.Item>
        </Form>
    );
};
