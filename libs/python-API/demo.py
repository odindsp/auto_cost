#!/usr/bin/python
#coding=utf-8

import os
import sys
import adx_auto_cost

class auto_cost:
	def __init__(self) : adx_auto_cost.init()
	def check(self) : return adx_auto_cost.check()
	def error(self) : return adx_auto_cost.error()
	def wait(self) : return adx_auto_cost.wait()
	
	def bid_create(self) : return adx_auto_cost.bid_create()
	def bid_write(self, mapid, adxcode, mediacode, regioncode, value) :
		return adx_auto_cost.bid_write(mapid, adxcode, mediacode, regioncode, value)
	def bid_flush(self) : return adx_auto_cost.bid_flush()
	def push(self, mess) : return adx_auto_cost.push(mess)

	def forge_count(self, policyid, timebucket, key, val) :
		return adx_auto_cost.forge_count(policyid, timebucket, key, val)
	
	def get_conf(self) : return adx_auto_cost.get_conf()
	def get_count(self, key) : return adx_auto_cost.get_conf(key)
    
class BID:
	auto_cost = None
	def __init__(self, auto_cost) : self.auto_cost = auto_cost
	def write(self, mapid, adxcode, mediacode, regioncode, value) :
		return self.auto_cost.bid_write(mapid, adxcode, mediacode, regioncode, value)
	def flush(self) : return self.auto_cost.bid_flush()




obj = auto_cost()
if (obj.check() == False) :
	print obj.error()
	sys.exit(0)

def auto_cost_loop():
	mess = obj.wait()
	info = mess['INFO']
	count = mess['COUNT']
	print mess

# while (True) : auto_cost_loop()

print obj.get_count("")


