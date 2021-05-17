import { User } from '../types';
import { isNil } from 'lodash';

export enum localStorageKeys {
    USER = 'user',
    ACCESS_KEY = 'access_key',
    ACCOUNT = 'account',
    EMAIL = 'email',
}

export const getCurrentUser = (): User | null => {
    const localUser: string | null = localStorage.getItem(localStorageKeys.USER);
    return !isNil(localUser) ? JSON.parse(localUser) : null;
};

export const setCurrentUser = (user: User): void => {
    localStorage.setItem(localStorageKeys.USER, JSON.stringify(user));
};
export const getEmail = (): string | null => {
    const localUser: string | null = localStorage.getItem(localStorageKeys.EMAIL);
    return !isNil(localUser) ? JSON.parse(localUser) : null;
};

export const setEmail = (email: string): void => {
    localStorage.setItem(localStorageKeys.EMAIL, JSON.stringify(email));
};
export const getAccessKey = (): string | null => {
    const localUser: string | null = localStorage.getItem(localStorageKeys.ACCESS_KEY);
    return !isNil(localUser) ? JSON.parse(localUser) : null;
};

export const setAccessKey = (key: string): void => {
    localStorage.setItem(localStorageKeys.ACCESS_KEY, JSON.stringify(key));
};
