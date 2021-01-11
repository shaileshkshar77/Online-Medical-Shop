class DBRouter1(object):

    def db_for_read(self,model, **hints):
        if model._meta.app_label == 'feedback':
            return 'feedbacks'
        return None

    def db_for_write(self,model, **hints):
        if model._meta.app_label == 'feedback':
            return 'feedbacks'
        return None

    def allow_relation(self,obj1, obj2, **hints):
        if obj1._meta.app_label == 'feedback' and \
           obj2._meta.app_label == 'feedback':
           return True
        return None

    def allow_syncdb(self,db, model):
        if db == 'feedbacks':
            if model._meta.app_label == 'feedback':
                return True
        elif model._meta.app_label == 'feedback':
            return False
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'feedback':
            return db == 'feedbacks'
        return None