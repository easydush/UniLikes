import React, { useEffect, useMemo, useState } from 'react';
import { Avatar, Badge, Layout, Table, Tag } from 'antd';
import { HeaderCustom } from '../../components/Header';
import { ColumnsType } from 'antd/lib/table';
import { Teacher } from '../../types/teacher';
import { getRatingStatus } from '../../utils/ratingStatus';
import { InfoBlock, PageHeaderText, StyledAlert, StyledContent, StyledPageHeader } from './styles';
import { getTeachers } from '../../api';
import { getCurrentTeachers } from '../../utils';

export const Main = (): JSX.Element => {
    const [loading, setLoading] = useState<boolean>(false);
    const [data, setData] = useState<Teacher[]>([]);

    const columns = useMemo(
        () =>
            [
                {
                    title: 'Фото',
                    dataIndex: 'photo',
                    width: '5%',
                    render: function renderAvatar(value, record) {
                        return <Avatar src={record.photo_url} />;
                    },
                },
                {
                    title: 'ФИО',
                    dataIndex: 'name',
                    width: '20%',
                    render: function renderName(value, record) {
                        return (
                            <p>
                                {record.surname} {record.name} {record.patronymic}
                            </p>
                        );
                    },
                    sorter: (a, b) => a.surname.localeCompare(b.surname),
                },
                {
                    title: 'Предметы',
                    dataIndex: 'subjects',
                    width: '50%',
                    render: function renderSubjects(value, record) {
                        return (
                            <>
                                {record.subjects.map((tag) => {
                                    const color = tag.length < 5 ? 'geekblue' : tag.length > 7 ? 'gold' : 'green';
                                    return (
                                        <Tag color={color} key={tag}>
                                            {tag.toUpperCase()}
                                        </Tag>
                                    );
                                })}
                            </>
                        );
                    },
                },
                {
                    title: 'Рейтинг',
                    dataIndex: 'rating',
                    render: function renderSubjects(value) {
                        return (
                            <p>
                                {' '}
                                <Badge status={getRatingStatus(value)} /> {value}
                            </p>
                        );
                    },
                    sorter: (a, b) => a.rating - b.rating,
                },
            ] as ColumnsType<Teacher>,
        [],
    );
    useEffect(() => {
        async function getData() {
            setLoading(true);
            await setTimeout(() => {
                getTeachers();
                setData(getCurrentTeachers() ?? []);
                setLoading(false);
            }, 500);
        }

        getData();
    }, []);
    return (
        <Layout>
            <HeaderCustom />
            <StyledContent>
                <StyledPageHeader title={<PageHeaderText>Рейтинг преподавателей</PageHeaderText>} backIcon={false} />
                <InfoBlock>
                    <StyledAlert
                        message="Информация"
                        description="Сейчас доступно голосование"
                        type="info"
                        showIcon
                        closable
                    />
                    <Table<Teacher>
                        columns={columns}
                        dataSource={data}
                        loading={loading}
                        pagination={{ pageSize: 7 }}
                    />
                </InfoBlock>
            </StyledContent>
        </Layout>
    );
};
