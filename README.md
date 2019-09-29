```javascript
{
    lr:{
        name:"Linear Regression",
        url:'/train/regression/linear',
        hyper_params:[
                {name:"fit_intercept",type:"bool",default:true},
                {name:"normalize",type:"bool",default:false},
                {name:"n_jobs",type:"num",data:[0,100,10]},
                {name:"cat_test",type:"cat",data:["a","b","c"]}
        ],
        type:"ml/supervised/regression/linear",
        par:"regression",
    },
}
```
