import axios, { AxiosInstance, AxiosRequestConfig, AxiosResponse } from 'axios';
import { localStorageKeys } from '../utils';

const getAxiosConfig = (): AxiosRequestConfig => {
    const token = localStorage.getItem(localStorageKeys.ACCESS_KEY);
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const headers: any = {};

    if (token) {
        headers.Authorization = `Bearer ${token}`;
    }

    return {
        baseURL: `${window.location.protocol}//${window.location.host}/`,
        headers,
    };
};

class ApiClient {
    private readonly instance: AxiosInstance;

    constructor() {
        this.instance = axios.create(getAxiosConfig());
    }

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    get(url: string, config?: AxiosRequestConfig): Promise<AxiosResponse<any>> {
        return this.instance.get(url, config);
    }

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    post(url: string, body: any, config?: AxiosRequestConfig): Promise<AxiosResponse<any>> {
        return this.instance.post(url, body, config);
    }

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    put(url: string, body: any, config?: AxiosRequestConfig): Promise<AxiosResponse<any>> {
        return this.instance.put(url, body, config);
    }

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    patch(url: string, body: any, config?: AxiosRequestConfig): Promise<AxiosResponse<any>> {
        return this.instance.patch(url, body, config);
    }

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    delete(url: string, config?: AxiosRequestConfig): Promise<AxiosResponse<any>> {
        return this.instance.delete(url, config);
    }

    setAuthHeader(token: string): void {
        this.instance.defaults.headers.Authorization = `Bearer ${token}`;
    }
}

export const apiClient = new ApiClient();
