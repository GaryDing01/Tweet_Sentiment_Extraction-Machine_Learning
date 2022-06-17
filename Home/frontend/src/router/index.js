import Vue from 'vue'
import Router from 'vue-router'
import MainPage from '@/components/MainPage'

import EmployeeLoginPage from '@/components/EmployeeAccount/EmployeeLoginPage'

//进入员工操作页面
import StaffEnter from '@/components/Enter/StaffEnter'

//个人信息
import EPersonalInfo from '@/components/People/EPersonalInfo'
import EChangePwd from '@/components/People/EChangePwd'

//员工管理
import StaffOverall from '@/components/People/StaffOverall'
import StaffSearch from '@/components/People/StaffSearch'
import StaffRewrite from '@/components/People/StaffRewrite'

//员工（新版本）
import StaffManagement from '@/components/People_new/StaffManagement'
import SidePer from '@/components/People_new/SidePer'
import AllManagement from '@/components/People_new/AllManagement'
import SalaryManagement from '@/components/People_new/SalaryManagement'

//测试
import test_p from '@/components/People_new/test_p'
import test_p2 from '@/components/People_new/test_p2'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'AllManagement',
      component: AllManagement
    },

    {
      path: '/EmployeeAccount/EmployeeLoginPage',
      name: 'EmployeeLoginPage',
      component: EmployeeLoginPage
    },


    {
      path: '/StaffEnter',
      name:'StaffEnter',
      component: StaffEnter,
      children:[
        //个人信息
        {
          path:'/EPersonalInfo',
          component:EPersonalInfo
        },
        {
          path:'/EChangePwd',
          component:EChangePwd
        },
        
        //员工
        {
          path:'/StaffOverall',
          component:StaffOverall
        },
        {
          path:'/StaffSearch',
          component:StaffSearch
        },
        {
          path:'/StaffRewrite',
          component:StaffRewrite
        },
        //员工（新版本）
        {
          path:'/StaffManagement',
          component:StaffManagement
        },
        {
          path:'/test_p',
          component:test_p
        },
        {
          path:'/test_p2',
          component:test_p2
        },
        {
          path:'/SidePer',
          component:SidePer
        },
        {
          path:'/AllManagement',
          component:AllManagement
        },
        {
          path:'/SalaryManagement',
          component:SalaryManagement
        },

      ]
    },

  ]
})
