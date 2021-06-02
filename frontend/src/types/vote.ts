export interface VoteTeacher {
    id: number;
    name: string;
    photo: string;
    subject: string;
}
export type VoteCredentials = {
    teacher_id: number,
    rate: number,
}
