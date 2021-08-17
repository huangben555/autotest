import {createStore} from "vuex";

const applyInfo = createStore({
    state: {
        applyNo: "1",
    },
    mutations: {
        setData(state, msg){
            state.applyNo = msg
        },
    },
});

export {applyInfo}