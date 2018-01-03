#-*- coding: utf8 -*-
# 异步写（md5分库）版本
import cPickle as pickle
#from sqlalchemy import select, and_, or_, func, not_
#from farm_lib.common.utils import cache

#from farm_lib.common import utils

#import dbhelper
#from tthelper import ttclient as _dbw_cache

#Db_adapter = dbhelper.Db_adapter
#__all__ = ['Model_Error', 'Serializer', 'Db_adapter', 'Model']


class Model_Error(Exception):
    """Exception class for Model"""

    def __init__(self, code, msg, data=None, args=None):
        if not isinstance(msg, unicode):
            msg = msg.decode('utf-8')
        self.code = code
        self.msg = msg
        self.data = data
        self.args = (args or [])

    def __str__(self):
        return (u'Error %s: %s' % (self.code, self.msg)).encode('utf-8')

class Serializer(object):
    def __init__(self):
        super(Serializer, self).__init__()
    
    @classmethod
    def get_seq_attrs(cls):
        if hasattr(cls, 'all_seq_attrs'):
            return getattr(cls, 'all_seq_attrs')
        
        if hasattr(cls, 'seq_attrs'):
            seq_attrs = getattr(cls, 'seq_attrs')[:]
        else:
            seq_attrs = []

        for base_cls in cls.__bases__:
            if hasattr(base_cls, 'seq_attrs'):
                seq_attrs.extend(getattr(base_cls, 'seq_attrs'))
        
        setattr(cls, 'all_seq_attrs', seq_attrs)
        return seq_attrs
    
    @classmethod
    def get_adv_seq_attrs(cls):
        if hasattr(cls, 'all_adv_seq_attrs'):
            return getattr(cls, 'all_adv_seq_attrs')

        if hasattr(cls, 'adv_seq_attrs'):
            seq_attrs = getattr(cls, 'adv_seq_attrs')[:]
        else:
            seq_attrs = []

        for base_cls in  cls.__bases__:
            if hasattr(base_cls, 'adv_seq_attrs'):
                seq_attrs.extend(getattr(base_cls, 'adv_seq_attrs'))
        
        setattr(cls, 'all_adv_seq_attrs', seq_attrs)
        return seq_attrs
    
    @classmethod
    def get_obj_seq_attrs(cls):
        #返回的是一个字典
        if hasattr(cls, 'all_obj_seq_attrs'):
            return getattr(cls, 'all_obj_seq_attrs')

        if hasattr(cls, 'obj_seq_attrs'):
            seq_attrs = getattr(cls, 'obj_seq_attrs').copy()
        else:
            seq_attrs = {}

        for base_cls in  cls.__bases__:
            if hasattr(base_cls, 'obj_seq_attrs'):
                seq_attrs.update(getattr(base_cls, 'obj_seq_attrs'))
        
        setattr(cls, 'all_obj_seq_attrs', seq_attrs)
        return seq_attrs

    @classmethod
    def loads(cls, data):
        """
            从一个字典（从数据库中直接获取的）中序列化出一个对象
        """

        seq_attrs = cls.get_seq_attrs()
        adv_seq_attrs = cls.get_adv_seq_attrs()
        obj_seq_attrs = cls.get_obj_seq_attrs()
        obj_seq_attr_names = [a for a in obj_seq_attrs]

        o = cls()
        for attr in seq_attrs:
            #数据库中没有这条记录的话使用默认值
            if not data.has_key(attr):
                continue
            if hasattr(cls, attr+'_loads'):
                setattr(o, attr, getattr(cls, attr+'_loads')(data[attr]))
            elif attr in adv_seq_attrs:
                if data[attr]:
                    setattr(o, attr, pickle.loads(str(data[attr])))
                else :
                    setattr(o, attr, None)
            elif attr in obj_seq_attr_names:
                attr_cls = obj_seq_attrs[attr]
                setattr(o, attr, attr_cls.loads(pickle.loads(data[attr])))
            else:
                setattr(o, attr, data[attr])
        
        return o
    
    @classmethod
    def loads_dict(cls, data):
        """
            从一个字典（从数据库中直接获取的）中序列化出一个字典
        """

        seq_attrs = cls.get_seq_attrs()
        adv_seq_attrs = cls.get_adv_seq_attrs()
        obj_seq_attrs = cls.get_obj_seq_attrs()
        obj_seq_attr_names = [a for a in obj_seq_attrs]

        o = {}
        for attr in seq_attrs:
            if not data.has_key(attr):
                continue
            if hasattr(cls, attr+'_loads'):
                o[attr] = getattr(cls, attr+'_loads')(data[attr])
            elif attr in adv_seq_attrs:
                if data[attr] :
                    o[attr] = pickle.loads(str(data[attr]))
                else :
                    o[attr] = None
            elif attr in obj_seq_attr_names:
                attr_cls = obj_seq_attrs[attr]
                o[attr] = attr_cls.loads(pickle.loads(data[attr]))
            else:
                o[attr] = data[attr]
        
        return o
    
    @classmethod
    def dumps_dict(cls, data, shallow = False):
        """
            从data中返回一个字典，字典的值跟数据库中一直
            如果shallow为true，则属性不进行pickle处理，这种情况一般用在发送到浏览器
        """
        seq_attrs = data.keys()

        adv_seq_attrs = cls.get_adv_seq_attrs()

        obj_seq_attrs = cls.get_obj_seq_attrs()
        obj_seq_attr_names = [a for a in obj_seq_attrs]

        if shallow:
            dumps = lambda x, y: x
        else:
            dumps = pickle.dumps

        res = {}
        
        def get_org_attr(attr):
            if attr.endswith('_gt') or attr.endswith('_lt') or attr.endswith('_lt') \
                        or attr.endswith('_lte') or attr.endswith('_gte') \
                        or attr.endswith('_not'):
                return attr[0:attr.rindex('_')]
            return attr

        for attr in seq_attrs:
            org_attr = get_org_attr(attr)
            if hasattr(cls, 'cls_'+org_attr+'_dumps'):
                res[attr] = getattr(cls, org_attr+'_dumps')(data[attr], shallow)
            elif org_attr in adv_seq_attrs:
                res[attr] = dumps(data[attr], -1)
            elif org_attr in obj_seq_attr_names:
                attr_cls = obj_seq_attrs[org_attr]
                res[attr] = dumps(data[attr].dumps(shallow), -1)
            else:
                res[attr] = data[attr]
        
        return res

    def dumps(self, attrs = None, shallow = False):
        """
            返回一个字典，字典的内容可以直接放到数据库中
            如果shallow为true，则属性不进行pickle处理，这种情况一般用在发送到浏览器 
        """
        if attrs is not None:
            seq_attrs = attrs
        else:
            seq_attrs = self.get_seq_attrs()

        adv_seq_attrs = self.get_adv_seq_attrs()

        obj_seq_attrs = self.get_obj_seq_attrs()
        obj_seq_attr_names = [a for a in obj_seq_attrs]

        if shallow:
            dumps = lambda x, y: x
        else:
            dumps = pickle.dumps

        res = {}
        for attr in seq_attrs:
            if hasattr(self, attr+'_dumps'):
                res[attr] = getattr(self, attr+'_dumps')(shallow)
            elif attr in adv_seq_attrs:
                res[attr] = dumps(getattr(self, attr), -1)
            elif attr in obj_seq_attr_names:
                attr_cls = obj_seq_attrs[attr]
                res[attr] = dumps(getattr(self, attr).dumps(shallow), -1)
            else:
                res[attr] = getattr(self, attr)
        
        return res


#class Model(Serializer):
#    """
#    以下属性需要子类实现
#    database = None
#    db_engine = None
#    is_multi_table = None
#    table_format = None
#    table_num = None
#    key_name_field = None
#    use_cache = None
#    cache_perfix = None
#    """
#    db = None
#    
#    def __init__(self):
#        super(Model, self).__init__()
#        self.is_saved = False
#    
#    @classmethod
#    def get_db(cls):
#        if cls.db:
#            return cls.db
#        else:
#            db = Db_adapter(cls)
#            cls.db = db
#            return db
#
#    def get_db_engine(self):
#        shard_index =  self.get_db().get_shard_index(self.get_key_name())
#        return self.database.all_dbs[shard_index]
#                            
#    def get_key_name(self):
#        return getattr(self, self.key_name_field)
#    
#    def get_cache_key(self):
#        return self.cache_perfix + "||" + self.__module__ + "." + self.__class__.__name__ + '||' + str(self.get_key_name())
#        
#    @classmethod
#    def generate_cache_key(cls, key_name):
#        return cls.cache_perfix + "||" + cls.__module__ + "." + cls.__name__ + '||' + str(key_name)
#
#    @classmethod
#    def get(cls, key_name, conn = None):
#        #获取cache_key
#        cache_key = cls.generate_cache_key(key_name)
#        
#        #尝试从memcached中获取
#        cache_value = cache.get(cache_key)
#        
#        #尝试从ttserver中获取
#        if not cache_value:
#            cache_value = _dbw_cache.get(cache_key)
#        
#        if cache_value:
#            res =  cache_value
#            o = cls.loads(res)
#            o.is_saved = True   #写数据库时用UPDATE，不用INSERT
#            return o
#        
#        #尝试从db中获取
#        res = cls.get_db().get(key_name, conn = conn)
#
#        if res is None:
#            return None
#        
#        o = cls.loads(res)  #反序列化成对象
#        o.is_saved = True   #保存时用UPDATE，不用INSERT
#        
#        cache_value = o.dumps()
#        
#        #写入memcached中，不写入ttserver
#        cache.set(cache_key, cache_value, 3600)
#        return o
#    
#    @classmethod
#    def query(cls, condition = None, offset = None, limit = None, order_by = None):
#        '''
#        根据某些条件进行查询，返回查询结果的枚举。
#        '''
#        if condition is None:
#            condition = {}
#        condition = cls.dumps_dict(condition)
#        for item in cls.get_db().query(condition, offset, limit, order_by):
#            o = cls.loads(item)
#            #检查在cache和ttserver中是否已存在
#            cache_key = o.get_cache_key()
#            res = cache.get(cache_key)
#            if not res:
#                res = _dbw_cache.get(cache_key)
#            if res:
#                #cache中已存在，以cache数据为准 
#                o = cls.loads(res)
#            else:
#                #cache中还没有，写入memcached不写入ttserver
#                cache_value = o.dumps()
#                cache.set(cache_key, cache_value, 3600)
#                
#            o.is_saved = True #保存时用UPDATE，不用INSERT
#            yield o
#
#
#    @classmethod
#    def gets(cls, key_names):
#        res = []
#        for key_name in key_names:
#            res.append(cls.get(key_name))
#        return res
#
#    @classmethod
#    def get_fields(cls, key_name, fields):
#        o = cls.get(key_name)
#        if o:
#            res = o.dumps()
#            return cls.loads_dict(res)
#        return None
#
#    @classmethod
#    def gets_fields(cls, key_names, fields):
#        res = []
#        for key in key_names:
#            r = cls.get_fields(key, fields)
#            if r:
#                res.append(r)
#        return res
#                
#    @classmethod
#    def exist(cls, key_name):
#        return cls.get_db().has_key(key_name)
#        
#
#    def put(self, conn = None, immediate = False):
#        '''
#        完整保存对象数据
#        '''
#        cache_key = self.get_cache_key() 
#        #清除memcached
#        for i in xrange(10):
#            ret = cache.delete(cache_key)
#            if ret > 0:
#                break
#        if ret == 0:
#            raise RuntimeError(1001, u'抱歉，数据缓存错误')    
#               
#        if not self.is_saved:   #尚未在数据库中保存过，立即INSERT
#            last_id = self.get_db().save(self.get_key_name(), self.dumps(), conn)
#            if self.get_key_name() is None:
#                setattr(self, self.key_name_field, last_id)
#            self.is_saved = True
#        elif immediate:         #立即写入数据库
#            self.get_db().update(self.get_key_name(), self.dumps(), conn)
#        
#        #写入ttserver和memcached
#        cache_value = self.dumps()
#        _dbw_cache.set(cache_key, cache_value)
#        cache.set(cache_key, cache_value, 3600) 
# 
#    def delete(self, conn = None):
#        cache_key = self.get_cache_key() 
#        cache.delete(cache_key)
#        _dbw_cache.delete(cache_key)        
#        self.get_db().delete(self.get_key_name(), conn)               
#        
#    @classmethod
#    def deletes(cls, objs, conn = None):
#        if len(objs) == 0:
#            return
#
#        if isinstance(objs[0], cls):
#            objs = [o.get_key_name() for o in objs]
#
#        for key_name in objs:
#            cache_key = cls.generate_cache_key(key_name)
#            cache.delete(cache_key)
#            _dbw_cache.delete(cache_key)
#                
#        cls.get_db().deletes(objs, conn)
#
#        
#    def update(self, attrs, conn = None, immediate = False):
#        '''
#        更新对象的部分属性
#        '''
#        #获取完整实例
#        full_obj = self.__class__.get(self.get_key_name()) or self
#        
#        for attr in attrs:
#            setattr(full_obj, attr, getattr(self, attr))
#             
#        full_obj.put(conn, immediate)
#                
#    @classmethod
#    def run_in_transaction(cls, *ops):
#        #ops: [[a, 'put'], [b, 'update', ['gold']]]
#        db_engines = {}
#        for op in ops:
#            db_engine = op[0].get_db_engine()
#            if not db_engines.has_key(db_engine):
#                db_engines[db_engine] = {'db': None, 'ops': [op]}
#            else:
#                db_engines[db_engine]['ops'].append(op)
#        
#        def rollback():
#            for db_engine in db_engines:
#                if db_engines[db_engine]['db']:
#                    try:
#                        db_engines[db_engine]['db'][1].rollback()
#                    except:
#                        pass
#        
#        def close():
#            for db_engine in db_engines:
#                if db_engines[db_engine]['db']:
#                    try:
#                        db_engines[db_engine]['db'][0].close()
#                    except:
#                        pass
#        
#        def commit():
#            for db_engine in db_engines:
#                try:
#                    db_engines[db_engine]['db'][1].commit()
#                except Exception, e:
#                    rollback()
#                    raise Model_Error(1000, u'数据库操作失败：%s'%e)
#
#        try:
#            has_error = cls._transaction2(db_engines)
#            if has_error:
#                for db_engine in db_engines:
#                    rollback()
#                raise Model_Error(1000, u'数据库操作失败')
#        except Exception, e:
#            rollback()
#            utils.print_err()
#            raise Model_Error(1000, u'数据库操作失败：%s'%e)
#        else:
#            commit()
#        finally:
#            close()
# 
#    @classmethod
#    def _transaction2(cls, db_engines):
#        has_error = False
#        for db_engine in db_engines:
#            conn = db_engine.connect()
#            trans = conn.begin()
#            db_engines[db_engine]['db'] = [conn, trans]
#            try:
#               for op in db_engines[db_engine]['ops']:
#                   if op[1] == 'put':
#                       op[0].put(conn, True)
#                   elif op[1] == 'update':
#                       op[0].update(op[2], conn, True)
#            except Exception, e:
#                has_error = True
#                utils.print_err()
#                break
#        
#        return has_error        
#
#    @classmethod
#    def count(cls, **condition):
#        condition = cls.dumps_dict(condition)
#        return cls.get_db().count(**condition)                