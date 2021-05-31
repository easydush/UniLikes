import { RegisterCredentials } from '../types';
import { apiClient } from './client';
import { AxiosResponse } from 'axios';
import { setEmail, setUnvotedTeachers } from '../utils';
import { message } from 'antd';

export const vote = (userCredentials: RegisterCredentials): void => {
    apiClient.post('auth/users/', userCredentials)
        .then((response: AxiosResponse) => {
            setEmail(response?.data.email);
            return response;
        })
        .catch(() => {
            message.error('Error with register');
        });
};
export const fetchUnvotedTeachers = (): void => {
    apiClient.get('voting/', {})
        .then((response: AxiosResponse) => {
            setUnvotedTeachers(response?.data?.results);
            return response;
        })
        .catch(() => {
            message.error('Error with getting teachers to vote');
        });
};
