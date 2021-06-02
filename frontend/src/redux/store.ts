import { Action, configureStore, ThunkAction } from '@reduxjs/toolkit';
import { logger } from 'redux-logger';

import { rootReducer } from './rootReducer';
import { RootState } from './RootState';

const store = configureStore({
    reducer: rootReducer,
    devTools: process.env.NODE_ENV !== 'production',
    middleware: (getDefaultMiddleware) => (
        process.env.NODE_ENV === 'production'
            ? getDefaultMiddleware()
            : getDefaultMiddleware().concat(logger)
    ),
});
export type AppDispatch = typeof store.dispatch
export type AppThunk = ThunkAction<void, RootState, null, Action<string>>
export default store;
