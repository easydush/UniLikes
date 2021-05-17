import React, { useCallback, useEffect, useMemo, useState } from 'react';
import { VoteTeacher } from '../../types/vote';
import { votingTeacher } from '../../mock/voting';
import { Spin } from 'antd';
import { LoadingWrapper } from './styles';
import { StyledAlert } from '../../pages/Main/styles';
import { VoteCard } from '../VoteCard';

export const VotingModule = (): JSX.Element => {
    const [loading, setLoading] = useState<boolean>(false);
    const [data, setData] = useState<VoteTeacher[]>();
    const [currentIndex, setCurrentIndex] = useState<number>(0);

    useEffect(() => {
        async function getData() {
            setLoading(true);
            await setTimeout(() => {
                setData(votingTeacher);
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
                    photo={data[currentIndex]?.photo}
                    name={data[currentIndex]?.name}
                    subject={data[currentIndex]?.subject}
                    onClick={onClickHandler}
                />
            );
        }
        return null;
    }, [data, currentIndex, onClickHandler]);

    return (
        <LoadingWrapper>
            {(!data || loading) && <Spin size="large" />}
            {(data?.length === 0 || currentIndex >= (data?.length ?? 1)) && (
                <StyledAlert
                    message="Информация"
                    description="Нет преподавателей для голосования"
                    type="info"
                    showIcon
                />
            )}
            {currentVoteTeacher}
        </LoadingWrapper>
    );
};
