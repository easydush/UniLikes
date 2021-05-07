import { ConfirmResetCredentials, RegisterCredentials, ResetCredentials, User, UserCredentials } from '../types';
import { apiClient } from './client';
import { AxiosResponse } from 'axios';
import { message } from 'antd';

export const authorize = (userCredentials: UserCredentials): void => {
  apiClient.post('auth/token/login/', userCredentials)
    .then((response: AxiosResponse) => {
      console.log(response);
    })
    .catch(() => {
      message.error('Error with login');
    });
};
export const register = (userCredentials: RegisterCredentials): void => {
  apiClient.post('auth/users/', userCredentials)
    .then((response: AxiosResponse) => {
      console.log(response);
    })
    .catch(() => {
      message.error('Error with register');
    });
};
export const logout = (): void => {
  apiClient.post('auth/token/logout/', {})
    .then((response: AxiosResponse) => {
      console.log(response);
    })
    .catch(() => {
      message.error('Error with logout');
    });
};
export const resendEmail = (email: string): void => {
  apiClient.post('auth/users/resend_activation/', { email })
    .then((response: AxiosResponse) => {
      console.log(response);
    })
    .catch(() => {
      message.error('Error with resending email');
    });
};
export const resetPassword = (email: string): void => {
  apiClient.post('auth/users/reset_password/', { email })
    .then((response: AxiosResponse) => {
      console.log(response);
    })
    .catch(() => {
      message.error('Error with resetting password');
    });
};
export const setPassword = (resetCredentials: ResetCredentials): void => {
  apiClient.post('auth/users/set_password/', resetCredentials)
    .then((response: AxiosResponse) => {
      console.log(response);
    })
    .catch(() => {
      message.error('Error with setting password');
    });
};
export const confirmResetPassword = (confirmCredentials: ConfirmResetCredentials): void => {
  apiClient.post('auth/users/reset_password_confirm/', confirmCredentials)
    .then((response: AxiosResponse) => {
      console.log(response);
    })
    .catch(() => {
      message.error('Error with confirm resetting password');
    });
};
export const activate = (uid: string, token: string): void => {
  apiClient.post('auth/users/activation/', { uid, token })
    .then((response: AxiosResponse) => {
      console.log(response);
    })
    .catch(() => {
      message.error('Error with activating user');
    });
};
export const userInfo = (): void => {
  apiClient.get('auth/users/me/')
    .then((response: AxiosResponse) => {
      const user: User = response.data;
      console.log(response);
    })
    .catch(() => {
      message.error('Error with activating user');
    });
};
