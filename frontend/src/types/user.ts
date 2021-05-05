export type User = {
    token: string,
}

export const EmptyUser: User = {
    token: '',
};

export type UserCredentials = {
    email: string,
    password: string,
}
