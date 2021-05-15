import React, { useCallback } from 'react';
import { Button, Form, Input } from 'antd';
import { authorize } from '../../api';
import { setCurrentUser } from '../../utils';
import { makeRequiredFormFieldRule } from '../../utils/formRules';

export const Login = (): JSX.Element => {

    const handleFinish = useCallback((values) => {
        const response = authorize(values);
        response.then(data => {
            if (data){
                setCurrentUser(data.data);
            }
        })
    }, []);

    return (
        <Form onFinish={handleFinish}>
            <Form.Item
                label='Email'
                name='email'
                rules={[makeRequiredFormFieldRule('Please input your email!')]}
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
