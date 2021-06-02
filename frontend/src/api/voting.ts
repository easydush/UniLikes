import { apiClient } from './client';
import { AxiosResponse } from 'axios';
import { setUnvotedTeachers } from '../utils';
import { message } from 'antd';
import { VoteCredentials } from '../types/vote';

export const vote = (voteCredentials: VoteCredentials): void => {
    apiClient.post('voting/', voteCredentials)
        .then((response: AxiosResponse) => {
            return response;
        })
        .catch(() => {
            message.error('Error with voting');
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
