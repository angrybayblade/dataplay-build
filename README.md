```json
{
    linear:{
        name:"Linear Regression",
        url:'/train/regression/linear',
        hyper_params:[
                {name:"fit_intercept",type:"bool",default:true},
                {name:"normalize",type:"bool",default:false},
                {name:"n_jobs",type:"num",data:[0,100,10]},
                {name:"cat_test",type:"cat",data:["a","b","c"]}
        ],
        type:"ml/supervised/regression",
        par:"regression",
    },
    svr:{
            name:'SVR',
            url:'/train/regression/svr',
            hyper_params:[
                {name:"C",type:"num",data:[0,100,0.5]},
                {name:"gamma",type:"num",data:[0.1,10,0.1]},
                {name:"kernel",type:"cat",data:['rbf','linear','poly','sigmoid', 'precomputed']},
            ],
            type:"ml/supervised/regression",
            par:"regression"
    },
    dtr:{
        name:'Desicion Tree Regressor',
        url:'/train/regression/dtr',
        hyper_params:[],
        type:"ml/supervised/regression",
        par:"regression"
    },
    rfr:{
        name:'Random Forest Regressor',
        url:'/train/regression/rfr',
        hyper_params:[],
        type:"ml/supervised/regression",
        par:"regression"
    },
    sgdr:{
        name:'SGD Regressor',
        url:'/train/regression/sgdr',
        hyper_params:[],
        type:"ml/supervised/regression",
        par:"regression"
    },
}
```
