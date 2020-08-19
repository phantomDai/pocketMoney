package com.company.project.model;

import javax.persistence.*;

public class Order {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    private String orderid;

    private String fenlei;

    private String dabao;

    private String time;

    private String good;

    /**
     * @return id
     */
    public Integer getId() {
        return id;
    }

    /**
     * @param id
     */
    public void setId(Integer id) {
        this.id = id;
    }

    /**
     * @return orderid
     */
    public String getOrderid() {
        return orderid;
    }

    /**
     * @param orderid
     */
    public void setOrderid(String orderid) {
        this.orderid = orderid;
    }

    /**
     * @return fenlei
     */
    public String getFenlei() {
        return fenlei;
    }

    /**
     * @param fenlei
     */
    public void setFenlei(String fenlei) {
        this.fenlei = fenlei;
    }

    /**
     * @return dabao
     */
    public String getDabao() {
        return dabao;
    }

    /**
     * @param dabao
     */
    public void setDabao(String dabao) {
        this.dabao = dabao;
    }

    /**
     * @return time
     */
    public String getTime() {
        return time;
    }

    /**
     * @param time
     */
    public void setTime(String time) {
        this.time = time;
    }

    /**
     * @return good
     */
    public String getGood() {
        return good;
    }

    /**
     * @param good
     */
    public void setGood(String good) {
        this.good = good;
    }
}