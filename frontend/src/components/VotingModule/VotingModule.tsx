import React, { useCallback, useEffect, useMemo, useState } from 'react';
import { Spin } from 'antd';
import { LoadingWrapper } from './styles';
import { StyledAlert } from '../../pages/Main/styles';
import { VoteCard } from '../VoteCard';
import { getUnvotedTeachers } from '../../utils';
import { Teacher } from '../../types/teacher';
import { fetchUnvotedTeachers, getTeachers } from '../../api';

export const VotingModule = (): JSX.Element => {
    const [loading, setLoading] = useState<boolean>(false);
    const [data, setData] = useState<Teacher[]>();
    const [currentIndex, setCurrentIndex] = useState<number>(0);

    useEffect(() => {
        async function getData() {
            fetchUnvotedTeachers()
            setLoading(true);
            console.log()
            await setTimeout(() => {
                setData(getUnvotedTeachers() ?? []);
                //setData([]);
                setLoading(false);
            }, 2000);
        }

        getData();
    }, []);

    const onClickHandler = useCallback(() => {
        setCurrentIndex(currentIndex + 1);
    }, [currentIndex]);

    const currentVoteTeacher = useMemo((): JSX.Element | null => {
        if (data && currentIndex < data.length) {
            return (
                <VoteCard
                    photo={data[currentIndex]?.photo_url}
                    name={data[currentIndex]?.name}
                    subjects={data[currentIndex]?.subjects}
                    onClick={onClickHandler}
                />
            );
        }
        return null;
    }, [data, currentIndex, onClickHandler]);

    return (
        <LoadingWrapper>
            {(!data || loading) && <Spin size='large' />}
            {(data?.length === 0 || currentIndex >= (data?.length ?? 1)) && (
                <StyledAlert
                    message='Информация'
                    description='Нет преподавателей для голосования'
                    type='info'
                    showIcon
                />
            )}
            {currentVoteTeacher}
        </LoadingWrapper>
    );
};
