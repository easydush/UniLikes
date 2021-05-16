import { Teacher } from '../types/teacher';

const getTeachers = (amount: number): Teacher[] => {
    const arr: Teacher[] = [];
    for (let i = 0; i < amount; i++) {
        arr.push({
            lastVote: '2021-02-05 08:28:36',
            middleName: `Middle_${i}`,
            name: `Name_${i}`,
            photo: 'https://www.noku.io/file/2018/01/icon_Marketing.png',
            rating: Math.round(Math.random() * 100),
            subjects: ['Math', 'Russian lang', 'Arch', 'Python'],
            surname: `Surname_${i}`,
        });
    }
    return arr;
};

export const teachers: Teacher[] = getTeachers(10);