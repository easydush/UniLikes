import { User } from '../types';
import { isNil } from 'lodash';

enum localStorageKeys {
    USER = 'user',
    ACCESS_KEY = 'access_key'
}

export const getCurrentUser = (): User | null => {
    const localUser: string | null = localStorage.getItem(localStorageKeys.USER);
    return !isNil(localUser) ? JSON.parse(localUser) : null;
};

export const setCurrentUser = (user: User): void => {
    localStorage.setItem(localStorageKeys.USER, JSON.stringify(user));
};

export const getAccessKey = (): string | null => {
    const localUser: string | null = localStorage.getItem(localStorageKeys.ACCESS_KEY);
    return !isNil(localUser) ? JSON.parse(localUser) : null;
};

export const setAccessKey = (key: string): void => {
    localStorage.setItem(localStorageKeys.ACCESS_KEY, JSON.stringify(key));
};
