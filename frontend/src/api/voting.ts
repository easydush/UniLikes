import { RegisterCredentials } from '../types';
import { apiClient } from './client';
import { AxiosResponse } from 'axios';
import { setEmail } from '../utils';
import { message } from 'antd';

export const vote = (userCredentials: RegisterCredentials): void => {
    apiClient.post('auth/users/', userCredentials)
        .then((response: AxiosResponse) => {
            setEmail(response?.data.email);
            return response
        })
        .catch(() => {
            message.error('Error with register');
        });
};
