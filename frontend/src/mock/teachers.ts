import { Teacher } from '../types/teacher';

const getTeachers = (amount: number): Teacher[] => {
    const arr: Teacher[] = [];
    for (let i = 0; i < amount; i++) {
        arr.push({
            patronymic: `Middle_${i}`,
            name: `Name_${i}`,
            photo_url: 'https://www.noku.io/file/2018/01/icon_Marketing.png',
            rating: Math.round(Math.random() * 100),
            id: Math.round(Math.random() * 100),
            subjects: ['Math', 'Russian lang', 'Arch', 'Python'],
            surname: `Surname_${i}`,
        });
    }
    return arr;
};

export const teachers: Teacher[] = getTeachers(10);
