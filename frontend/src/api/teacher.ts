import { apiClient } from './client';
import { AxiosResponse } from 'axios';
import { message } from 'antd';
import { setTeachers } from '../utils';

export const getTeachers = (): void => {
    apiClient.get('teacher/', {})
        .then((response: AxiosResponse) => {
            console.log(response?.data?.results);
            setTeachers(response?.data?.results);
        })
        .catch(() => {
            message.error('Error with getting teachers');
        });
};
