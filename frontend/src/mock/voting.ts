import { VoteTeacher } from '../types/vote';

const getTeachers = (amount: number): VoteTeacher[] => {
    const arr: VoteTeacher[] = [];
    for (let i = 0; i < amount; i++) {
        arr.push({
            name: `Name_${i}`,
            photo: `https://picsum.photos/id/${i}/300/300`,
            subject: 'Math',
            id: i,
        });
    }
    return arr;
};

const Isis: VoteTeacher = {
    id: 0,
    name: 'Изидушка',
    photo: 'https://avatars.githubusercontent.com/u/45292943?v=4',
    subject: 'Мягкие лапки',
};

export const votingTeacher: VoteTeacher[] = [Isis, ...getTeachers(1)];
