import { Layout } from 'antd';
import { HeaderCustom } from '../../components/Header';
import React from 'react';
import { PageHeaderText, StyledContent, StyledPageHeader } from '../Main/styles';
import { VotingModule } from '../../components/VotingModule';

export const Voting = () : JSX.Element => {
    return (
        <Layout>
            <HeaderCustom />
            <StyledContent>
                <StyledPageHeader title={<PageHeaderText>Голосование</PageHeaderText>} backIcon={false} />
                <VotingModule />
            </StyledContent>
        </Layout>
    )
}