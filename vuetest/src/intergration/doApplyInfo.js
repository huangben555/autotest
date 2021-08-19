import {createStore} from "vuex";

const doApplyInfo = createStore({
    state: {
        applyNo: "",
    },
    mutations: {
        setData(state, msg){
            state.applyNo = msg
        },
    },
});

export {doApplyInfo}