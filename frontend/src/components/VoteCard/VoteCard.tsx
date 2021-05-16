import React, { useCallback } from 'react';
import { Card, message } from 'antd';
import Meta from 'antd/lib/card/Meta';
import { NegativeButton, NeutralButton, PositiveButton } from './styles';

interface VoteCardProps {
    photo?: string;
    name?: string;
    subject?: string;
    onClick: (event: MouseEvent) => void;
}

export const VoteCard = ({ photo, name, subject, onClick }: VoteCardProps): JSX.Element => {
    const onNegativeClick = useCallback(
        (event) => {
            onClick(event);
            message.error('Очень жаль', 2)
        },
        [onClick],
    );

    const onNeutralClick = useCallback(
        (event) => {
            onClick(event);
            message.warn('Нормально', 2)
        },
        [onClick],
    );

    const onPositiveClick = useCallback(
        (event) => {
            onClick(event);
            message.success('Отлично', 2)
        },
        [onClick],
    );

    return (
        <Card
            style={{ width: '30%' }}
            cover={<img alt="example" src={photo ? photo : ''} />}
            actions={[
                <NegativeButton key="negative" onClick={onNegativeClick}>
                    Негативно
                </NegativeButton>,
                <NeutralButton key="neutral" onClick={onNeutralClick}>
                    Нейтрально
                </NeutralButton>,
                <PositiveButton key="positive" onClick={onPositiveClick}>
                    Положительно
                </PositiveButton>,
            ]}
        >
            <Meta title={name ? name : ''} description={subject ? subject : ''} />
        </Card>
    );
};
