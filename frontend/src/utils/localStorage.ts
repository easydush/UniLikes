import { User } from '../types';
import { isNil } from 'lodash';
import { Teacher } from '../types/teacher';

export enum localStorageKeys {
    USER = 'user',
    ACCESS_KEY = 'access_key',
    ACCOUNT = 'account',
    EMAIL = 'email',
    TEACHERS = 'teachers',
}

export const getCurrentUser = (): User | null => {
    const localUser: string | null = localStorage.getItem(localStorageKeys.USER);
    return !isNil(localUser) ? JSON.parse(localUser) : null;
};

export const setCurrentUser = (user: User): void => {
    localStorage.setItem(localStorageKeys.USER, JSON.stringify(user));
};
export const setCurrentAccount = (user: Account): void => {
    localStorage.setItem(localStorageKeys.ACCOUNT, JSON.stringify(user));
};
export const getCurrentAccount = (): Account | null => {
    const localUser: string | null = localStorage.getItem(localStorageKeys.ACCOUNT);
    return !isNil(localUser) ? JSON.parse(localUser) : null;
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
export const setTeachers = (teachers: Teacher[]): void => {
    localStorage.setItem(localStorageKeys.TEACHERS, JSON.stringify(teachers));
};
export const getCurrentTeachers = (): Teacher[] | null => {
    const teachers: string | null = localStorage.getItem(localStorageKeys.TEACHERS);
    return !isNil(teachers) ? JSON.parse(teachers) : null;
};
